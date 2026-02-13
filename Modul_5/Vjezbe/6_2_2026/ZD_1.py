import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.utils import image_dataset_from_directory
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns

# 1. POSTAVLJANJE PUTANJA
# Koristimo apsolutnu putanju kako bismo izbjegli probleme s radnim direktorijem
base_path = os.path.dirname(os.path.abspath(__file__))
train_dir = os.path.join(base_path, 'gtsrb', 'train')
val_dir = os.path.join(base_path, 'gtsrb', 'val')
test_dir = os.path.join(base_path, 'gtsrb', 'test')

img_size = (48, 48)
batch_size = 32

# 2. UČITAVANJE PODATAKA
print("Učitavanje podataka...")
train_ds = image_dataset_from_directory(train_dir, image_size=img_size, batch_size=batch_size, label_mode='int')
val_ds = image_dataset_from_directory(val_dir, image_size=img_size, batch_size=batch_size, label_mode='int')
# Kod testnog skupa shuffle MORA biti False zbog matrice zabune
test_ds = image_dataset_from_directory(test_dir, image_size=img_size, batch_size=batch_size, label_mode='int', shuffle=False)

class_names = train_ds.class_names
num_classes = len(class_names)

# 3. IZRADA MODELA (Prema tvojoj shemi: 32-64-128)
inputs = tf.keras.Input(shape=(48, 48, 3))
x = layers.Rescaling(1./255)(inputs)

# Blok 1
x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
x = layers.Conv2D(32, (3, 3), activation='relu', padding='valid')(x)
x = layers.MaxPooling2D((2, 2))(x)
x = layers.Dropout(0.2)(x)

# Blok 2
x = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(x)
x = layers.Conv2D(64, (3, 3), activation='relu', padding='valid')(x)
x = layers.MaxPooling2D((2, 2))(x)
x = layers.Dropout(0.2)(x)

# Blok 3
x = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(x)
x = layers.Conv2D(128, (3, 3), activation='relu', padding='valid')(x)
x = layers.MaxPooling2D((2, 2))(x)
x = layers.Dropout(0.2)(x)

# Izlazni dio
x = layers.Flatten()(x)
x = layers.Dense(2048, activation='relu')(x)
x = layers.Dense(512, activation='relu')(x)
x = layers.Dropout(0.5)(x)
outputs = layers.Dense(num_classes, activation='softmax')(x)

model = tf.keras.Model(inputs=inputs, outputs=outputs)

model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])

# 4. TRENIRANJE
epochs = 10
print(f"Početak treniranja na {epochs} epoha...")
history = model.fit(train_ds, validation_data=val_ds, epochs=epochs)

# 5. SPREMANJE MODELA
model_name = 'model_gtsrb_final.h5'
model.save(model_name)
print(f"\n✅ Model je spremljen kao: {model_name}")

# 6. EVALUACIJA I MATRICA ZABUNE
print("\nIzračunavanje predviđanja za testni skup...")
y_pred_probs = model.predict(test_ds)
y_pred = np.argmax(y_pred_probs, axis=1)
y_true = np.concatenate([y for x, y in test_ds], axis=0)

# Matrica zabune
cm = confusion_matrix(y_true, y_pred)
plt.figure(figsize=(16, 12))
sns.heatmap(cm, annot=False, cmap='Blues')
plt.xlabel('Predviđeno')
plt.ylabel('Stvarno')
plt.title('Matrica Zabune (Confusion Matrix)')
plt.savefig('matrica_zabune.png') # Sprema sliku matrice
plt.show()

# Classification report (tekstualni prikaz preciznosti po klasi)
print("\nIzvještaj klasifikacije:")
print(classification_report(y_true, y_pred, target_names=class_names))

# 7. PRIKAZ GRAFOVA TOČNOSTI
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Trening Accuracy')
plt.plot(history.history['val_accuracy'], label='Validacija Accuracy')
plt.title('Točnost kroz epohe')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Trening Loss')
plt.plot(history.history['val_loss'], label='Validacija Loss')
plt.title('Gubitak kroz epohe')
plt.legend()
plt.show()