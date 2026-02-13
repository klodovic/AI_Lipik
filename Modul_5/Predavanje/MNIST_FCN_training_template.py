'''
Handwritten digits classification; MNIST dataset
Build, train and evaluate fully connected neural network in Keras

R.Grbic
'''


from tensorflow import keras
import keras
from keras import layers
from matplotlib import pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report



# load the MNIST data
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data(path="mnist.npz")
print("Original x_train shape", x_train.shape)
print("Original y_train shape", y_train.shape)


# Scale input data (x_train and x_test) to [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255


# Reshape x_train and x_test for shape required by fully connected network
x_train_s = x_train_s.reshape(60000, 784)
x_test_s = x_test_s.reshape(10000, 784)


# appy one hot encoding to y_train and y_test
y_train_s = keras.utils.to_categorical(y_train, 10)
y_test_s = keras.utils.to_categorical(y_test, 10)


# TODO: show single train image and print its class to terminal
for i in range(9):
	plt.subplot(330 + 1 + i)
	plt.imshow(x_train[i], cmap=plt.get_cmap('gray'))
plt.show()



# TODO: build neural network; write down number of parameters for each layer
model = keras.Sequential()
model.add(layers.Input(shape=(784, )))
model.add(layers.Dense(128, activation="relu"))
model.add(layers.Dense(32, activation="relu"))
model.add(layers.Dense(10, activation="softmax"))



# TODO: check model structure and parameteres with .summary() method
model.summary()



# TODO: configure training with .compile() method
model.compile(loss="categorical_crossentropy",
              optimizer="adam",
              metrics=["accuracy",])



# TODO: train network using history = model.fit(....
# use 10% of the training data for validation
batch_size = 64
epochs = 15
history = model.fit(x_train_s,
                    y_train_s,
                    batch_size = batch_size,
                    epochs = epochs,
                    validation_split = 0.1)



# TODO: show on same image train and val loss; show on same image train and val accuracy 
plt.figure(1, figsize=(14,5))
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



# TODO: evaluate built network on test data; print in terminal test loss and test accuracy
score = model.evaluate(x_test_s, y_test_s, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])



# TODO: make predictions for test data set
predicted_classes = np.argmax(model.predict(x_test_s), axis = -1)



# TODO: calculate metrics and confusion matrix on test dataset; use functions from scikit-learn
conf_matrix = confusion_matrix(y_test, predicted_classes)
print(conf_matrix)
print(classification_report(y_test, predicted_classes))



# TODO: save model to disk
#model.save("FCN/")
model.export("FCN")
