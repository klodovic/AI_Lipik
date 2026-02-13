'''
Zadatak 3
Evaluacija CNN-a na vlastitim slikama znamenki
'''

from tensorflow import keras
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import os

# -------------------------------------------------
# SETTINGS
# -------------------------------------------------
MODEL_PATH = "CNN_MNIST.keras"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "nums", "1.jpg") # promijeni u svoju sliku
  
# -------------------------------------------------
# LOAD MODEL
# -------------------------------------------------
model = keras.models.load_model(MODEL_PATH)
print("Model loaded.")

# -------------------------------------------------
# LOAD & PREPROCESS IMAGE
# -------------------------------------------------
# Open image and convert to grayscale
img = Image.open(IMAGE_PATH).convert("L")

# Resize (sigurnosno, ako nije točno 28x28)
img = img.resize((28, 28))

# Convert to numpy array
img_array = np.array(img).astype("float32")

# Normalize to [0,1]
img_array /= 255.0

# MNIST ima bijelu znamenku na crnoj pozadini
# Ako su tvoje slike crne na bijelom, invertiraj:
#img_array = 1.0 - img_array

# Reshape to CNN input shape
img_array = img_array.reshape(1, 28, 28, 1)

# -------------------------------------------------
# PREDICT
# -------------------------------------------------
predictions = model.predict(img_array)[0]
predicted_class = np.argmax(predictions)

print("Predicted class:", predicted_class)

# -------------------------------------------------
# SHOW IMAGE + BAR CHART OUTPUTS
# -------------------------------------------------
plt.figure(figsize=(10,4))

# Original image
plt.subplot(1,2,1)
plt.imshow(img_array.reshape(28,28), cmap="gray")
plt.title(f"Predicted: {predicted_class}")
plt.axis("off")

# Network outputs
plt.subplot(1,2,2)
plt.bar(range(10), predictions)
plt.xticks(range(10))
plt.xlabel("Digit class")
plt.ylabel("Softmax probability")
plt.title("Network output probabilities")

plt.show()
