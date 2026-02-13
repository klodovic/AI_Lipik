import os
import datetime
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.utils import image_dataset_from_directory
# Importi za callbackove (Zadatak 3)
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau, TensorBoard

# 1. POSTAVLJANJE PUTANJA
base_path = os.path.dirname(os.path.abspath(__file__))
train_dir = os.path.join(base_path, 'gtsrb', 'train')
val_dir = os.path.join(base_path, 'gtsrb', 'val')

img_size = (48, 48)
batch_size = 32

# 2. UČITAVANJE PODATAKA
train_ds = image_dataset_from_directory(train_dir, image_size=img_size, batch_size=batch_size, label_mode='int')
val_ds = image_dataset_from_directory(val_dir, image_size=img_size, batch_size=batch_size, label_mode='int')

num_classes = len(train_ds.class_names)

# 3. DEFINIRANJE CALLBACKOVA (Zadatak 3 - Implementacija)
# 1. EarlyStopping: nakon što se val_loss ne poboljša unutar 5 epoha
early_stop = EarlyStopping(
    monitor='val_loss', 
    patience=5, 
    restore_best_weights=True,
    verbose=1
)

# 2. ModelCheckpoint: spremanje samo najboljeg modela na temelju val_accuracy metrike
checkpoint = ModelCheckpoint(
    filepath='najbolji_model_gtsrb.h5',
    monitor='val_accuracy',
    save_best_only=True,
    mode='max',
    verbose=1
)

# 3. ReduceLROnPlateau: ako se val_loss ne smanji unutar 3 epohe, smanjiti LR za faktor 0.1
reduce_lr = ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.1,
    patience=3,
    min_lr=1e-6,
    verbose=1
)

# 4. TensorBoard: praćenje tijeka treninga
log_dir = os.path.join("logs", datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)

# Lista svih callbackova za fit metodu
my_callbacks = [early_stop, checkpoint, reduce_lr, tensorboard_callback]

# 4. MODEL (Arhitektura iz Zadatka 1)
inputs = tf.keras.Input(shape=(48, 48, 3))
x = layers.Rescaling(1./255)(inputs)

# Blokovi konvolucije
x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
x = layers.Conv2D(32, (3, 3), activation='relu', padding='valid')(x)
x = layers.MaxPooling2D((2, 2))(x)
x = layers.Dropout(0.2)(x)

x = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(x)
x = layers.Conv2D(64, (3, 3), activation='relu', padding='valid')(x)
x = layers.MaxPooling2D((2, 2))(x)
x = layers.Dropout(0.2)(x)

x = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(x)
x = layers.Conv2D(128, (3, 3), activation='relu', padding='valid')(x)
x = layers.MaxPooling2D((2, 2))(x)
x = layers.Dropout(0.2)(x)

# Klasifikator
x = layers.Flatten()(x)
x = layers.Dense(2048, activation='relu')(x)
x = layers.Dense(512, activation='relu')(x)
x = layers.Dropout(0.5)(x)
outputs = layers.Dense(num_classes, activation='softmax')(x)

model = tf.keras.Model(inputs=inputs, outputs=outputs)

model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])

# 5. POKRETANJE TRENINGA S CALLBACKOVIMA
print("\n--- Početak treniranja s callbackovima ---")
model.fit(
    train_ds, 
    validation_data=val_ds, 
    epochs=50,  # Postavljeno na više jer će EarlyStopping prekinuti po potrebi
    callbacks=my_callbacks
)


"""
Kako provjeriti rezultate (Točka 4)?

Nakon što trening završi (ili dok još traje), otvori novi Anaconda Prompt i upiši:

    Pozicioniraj se u mapu projekta:
    Bash

    cd c:\Users\******\Desktop\AI_Lipik\Modul_5\Vjezbe\6_2_2026

    Pokreni TensorBoard:
    Bash

    tensorboard --logdir logs

    Otvori browser (Chrome/Edge) i upiši: http://localhost:6006

Tamo ćeš vidjeti interaktivne grafove za Loss i Accuracy. Vidjet ćeš točno u kojoj je epohi ReduceLROnPlateau 
smanjio learning rate (graf će postati "mirniji") i gdje je EarlyStopping odlučio da je kraj.
"""