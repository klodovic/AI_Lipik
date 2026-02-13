"""
1. Učitaj jedan od postojećih modela u Keras-u (npr. Resnet50 ili MobileNetV2)
• koristite opcije: weights: „imagenet”, include_top = True
2. učitajte proizvoljnu sliku (npr. sliku automobila, banane, stolice ...) pomoću Keras
funkcije load_img
3. Napravite odgovarajuću predobradu učitane slike (img_to_array, expand_dims,
preprocess_input) te izvršite predikciju pomoću odabranog modela.
4. Budući da se radi o mrežni naučenoj na ImageNet-u, pomoću funkcije
keras.applications.imagenet_utils.decode_predictions
pretvorite predikciju u odgovarajuću klasu
5. „igrajte” se s mrežom (Izvršite inferenciju nad više različitih slika i analizirajte rezultate)
6. Uočavate li razlike u točnosti klasifikacije između različitih mrežnih arhitektura?

"""




import keras
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.applications.xception import Xception
from keras.applications.xception import preprocess_input, decode_predictions
import numpy as np

#model = ResNet50(weights='imagenet')

model = keras.applications.Xception(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
    name="xception",
)



img_path = 'bird.jpg'
img = keras.utils.load_img(img_path, target_size=(299, 299))
x = keras.utils.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = model.predict(x)
# decode the results into a list of tuples (class, description, probability)
# (one such list for each sample in the batch)
print('Predicted:', decode_predictions(preds, top=3)[0])
# Predicted: [(u'n02504013', u'Indian_elephant', 0.82658225), (u'n01871265', u'tusker', 0.1122357), (u'n02504458', u'African_elephant', 0.061040461)]


