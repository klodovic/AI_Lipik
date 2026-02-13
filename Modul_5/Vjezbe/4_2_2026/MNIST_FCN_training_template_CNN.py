'''
Handwritten digits classification; MNIST dataset
Convolutional Neural Network in Keras

'''

from tensorflow import keras
from keras import layers
from matplotlib import pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data(path="mnist.npz")

print("Original x_train shape:", x_train.shape)
print("Original y_train shape:", y_train.shape)

# -------------------------------------------------
# PREPROCESSING
# -------------------------------------------------
# Scale to [0,1]
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Reshape for CNN: (N, 28, 28, 1)
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# One-hot encoding
y_train_s = keras.utils.to_categorical(y_train, 10)
y_test_s = keras.utils.to_categorical(y_test, 10)

# -------------------------------------------------
# SHOW SAMPLE IMAGES
# -------------------------------------------------
for i in range(9):
    plt.subplot(330 + 1 + i)
    plt.imshow(x_train[i].reshape(28, 28), cmap="gray")
    plt.title(f"Class: {y_train[i]}")
    plt.axis("off")
plt.show()

# -------------------------------------------------
# BUILD CNN MODEL
# -------------------------------------------------
model = keras.Sequential()

# Input layer
model.add(layers.Input(shape=(28, 28, 1)))

# 1st Convolution block
model.add(layers.Conv2D(32, kernel_size=(3,3), padding="same", activation="relu"))
model.add(layers.MaxPooling2D(pool_size=(2,2)))

# 2nd Convolution block
model.add(layers.Conv2D(64, kernel_size=(3,3), padding="same", activation="relu"))
model.add(layers.MaxPooling2D(pool_size=(2,2)))

# Fully connected part
model.add(layers.Flatten())
model.add(layers.Dense(200, activation="relu"))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(50, activation="relu"))
model.add(layers.Dense(10, activation="softmax"))

# -------------------------------------------------
# MODEL SUMMARY
# -------------------------------------------------
model.summary()

# -------------------------------------------------
# COMPILE MODEL
# -------------------------------------------------
model.compile(
    loss="categorical_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)

# -------------------------------------------------
# TRAIN MODEL
# -------------------------------------------------
batch_size = 64
epochs = 15

history = model.fit(
    x_train,
    y_train_s,
    batch_size=batch_size,
    epochs=epochs,
    validation_split=0.1
)

# -------------------------------------------------
# PLOT LOSS & ACCURACY
# -------------------------------------------------
plt.figure(figsize=(14,5))

plt.subplot(1,2,1)
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='val')
plt.xlabel('Epoch')
plt.ylabel('Cross-Entropy Loss')
plt.legend()

plt.subplot(1,2,2)
plt.plot(history.history['accuracy'], label='train')
plt.plot(history.history['val_accuracy'], label='val')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.show()

# -------------------------------------------------
# EVALUATE MODEL
# -------------------------------------------------
score = model.evaluate(x_test, y_test_s, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])

# -------------------------------------------------
# CONFUSION MATRIX & CLASSIFICATION REPORT
# -------------------------------------------------
predicted_classes = np.argmax(model.predict(x_test), axis=-1)

conf_matrix = confusion_matrix(y_test, predicted_classes)
print("Confusion Matrix:")
print(conf_matrix)

print("\nClassification Report:")
print(classification_report(y_test, predicted_classes))

# -------------------------------------------------
# SAVE MODEL
# -------------------------------------------------
model.save("CNN_MNIST.keras")
