'''
Zadatak 2
Ucitavanje trenirane CNN mreze i evaluacija na MNIST test skupu
'''

from tensorflow import keras
from matplotlib import pyplot as plt
import numpy as np
import random

# -------------------------------------------------
# LOAD MODEL
# -------------------------------------------------
model = keras.models.load_model("CNN_MNIST.keras")
print("Model loaded successfully.")

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data(path="mnist.npz")

# Preprocessing (mora biti IDENTIČAN kao u treningu)
x_test = x_test.astype("float32") / 255.0
x_test = x_test.reshape(-1, 28, 28, 1)

# -------------------------------------------------
# PREDICTIONS
# -------------------------------------------------
predictions = model.predict(x_test)
predicted_classes = np.argmax(predictions, axis=1)

# -------------------------------------------------
# FIND CORRECT AND WRONG PREDICTIONS
# -------------------------------------------------
correct_idx = np.where(predicted_classes == y_test)[0]
wrong_idx = np.where(predicted_classes != y_test)[0]

# -------------------------------------------------
# SHOW 9 CORRECT CLASSIFICATIONS
# -------------------------------------------------
plt.figure(figsize=(8,8))
random_correct = random.sample(list(correct_idx), 9)

for i, idx in enumerate(random_correct):
    plt.subplot(3, 3, i + 1)
    plt.imshow(x_test[idx].reshape(28,28), cmap="gray")
    plt.title(f"Pred: {predicted_classes[idx]} | True: {y_test[idx]}")
    plt.axis("off")

plt.suptitle("Correctly classified test images")
plt.show()

# -------------------------------------------------
# SHOW 9 WRONG CLASSIFICATIONS
# -------------------------------------------------
plt.figure(figsize=(8,8))
random_wrong = random.sample(list(wrong_idx), 9)

for i, idx in enumerate(random_wrong):
    plt.subplot(3, 3, i + 1)
    plt.imshow(x_test[idx].reshape(28,28), cmap="gray")
    plt.title(f"Pred: {predicted_classes[idx]} | True: {y_test[idx]}")
    plt.axis("off")

plt.suptitle("Misclassified test images")
plt.show()
