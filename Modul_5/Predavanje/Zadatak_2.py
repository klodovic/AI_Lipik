import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score

# Učitavanje CIFAR-10 skupa (50k train + 10k test), slike su 32x32 RGB, y su label-e 0-9
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# Brza vizualna provjera nekoliko uzoraka
plt.figure(figsize=(6, 6))
for i in range(9):
    plt.subplot(3, 3, i + 1)
    plt.xticks([]), plt.yticks([])
    plt.imshow(X_train[i + 220])
plt.tight_layout()
plt.show()

# Normalizacija piksela u [0,1]
X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0

# Pretvaranje labela u one-hot (potrebno za categorical_crossentropy)
y_train_cat = to_categorical(y_train)
y_test_cat = to_categorical(y_test)
y_test_int = y_test.squeeze()

# Nazivi klasa 
class_names = [
    "airplane", "automobile", "bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck"
]

# Split train -> train/val (10% za validaciju), stratify čuva omjere klasa
X_train_f, X_val, y_train_f, y_val = train_test_split(
    X_train, y_train_cat, test_size=0.1, random_state=42, stratify=y_train
)

def conv_block(x, filters, dropout):
    x = layers.Conv2D(filters, 3, padding="same", use_bias=False)(x)
    x = layers.BatchNormalization()(x)
    x = layers.ReLU()(x)

    x = layers.Conv2D(filters, 3, padding="same", use_bias=False)(x)
    x = layers.BatchNormalization()(x)
    x = layers.ReLU()(x)

    x = layers.MaxPooling2D(2)(x)
    x = layers.Dropout(dropout)(x)
    return x

inputs = keras.Input(shape=(32, 32, 3))
x = conv_block(inputs, 32, 0.15)
x = conv_block(x, 64, 0.20)
x = conv_block(x, 128, 0.30)

x = layers.GlobalAveragePooling2D()(x)
x = layers.Dense(128, use_bias=False)(x)
x = layers.BatchNormalization()(x)
x = layers.ReLU()(x)
x = layers.Dropout(0.4)(x)
outputs = layers.Dense(10, activation="softmax")(x)

# Sastavljanje modela (Functional API)
model = keras.Model(inputs, outputs)
model.summary()

# Kompilacija: Adam (1e-3) kao dobar default; loss za multi-class one-hot; pratimo accuracy
model.compile(
    optimizer=keras.optimizers.Adam(1e-3),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

earlystop_cb = keras.callbacks.EarlyStopping(
    monitor="val_loss", patience=6, restore_best_weights=True, verbose=1
)
reduce_lr_cb = keras.callbacks.ReduceLROnPlateau(
    monitor="val_loss", factor=0.5, patience=3, min_lr=1e-6, verbose=1
)
tensorboard_cb = keras.callbacks.TensorBoard(
    log_dir="logs/cifar10_cnn_better", update_freq="epoch"
)

# Treniranje na train splitu, validacija na val splitu;
history = model.fit(
    X_train_f, y_train_f,
    validation_data=(X_val, y_val),
    epochs=50,
    batch_size=64,
    callbacks=[earlystop_cb, reduce_lr_cb, tensorboard_cb],
    verbose=1
)

# Vizualizacija učenja: loss i accuracy za train/val
plt.figure(figsize=(14, 5))
plt.subplot(1, 2, 1)
plt.plot(history.history["loss"], label="train")
plt.plot(history.history["val_loss"], label="val")
plt.xlabel("Epoha"); plt.ylabel("Loss")
plt.legend(); plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(history.history["accuracy"], label="train")
plt.plot(history.history["val_accuracy"], label="val")
plt.xlabel("Epoha"); plt.ylabel("Accuracy")
plt.legend(); plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Evaluacija na test skupu (neviđeni podaci)
test_loss, test_acc = model.evaluate(X_test, y_test_cat, verbose=0)
print(f"\nTEST -> loss: {test_loss:.4f}, accuracy: {test_acc:.4f}")

y_prob = model.predict(X_test, verbose=0)
y_pred = np.argmax(y_prob, axis=1)

cm = confusion_matrix(y_test_int, y_pred)
print("\nMatrica zabune:")
print(cm)

acc = accuracy_score(y_test_int, y_pred)
prec = precision_score(y_test_int, y_pred, average="macro", zero_division=0)
rec = recall_score(y_test_int, y_pred, average="macro", zero_division=0)
f1 = f1_score(y_test_int, y_pred, average="macro", zero_division=0)

print("\nMetrike (macro average):")
print(f"Accuracy : {acc:.4f}")
print(f"Precision: {prec:.4f}")
print(f"Recall   : {rec:.4f}")
print(f"F1-score : {f1:.4f}")

print("\nClassification report:")
print(classification_report(y_test_int, y_pred, target_names=class_names, zero_division=0))

print("\nTensorBoard: tensorboard --logdir logs")
