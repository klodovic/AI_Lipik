import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class MyComputerVision:

    def __init__(self):
        pass

    @staticmethod
    def load_image(image_path: str) -> np.ndarray:
        """
        Koristeći PIL modula učitati sliku s putanje <image_path>. Pretvoriti sliku u Numpy array.
        Kao povratnu vrijednost vratiti Numpy array učitane slike
        """
        img = Image.open(image_path)
        return np.asarray(img)

    @staticmethod
    def show_image(image: np.ndarray) -> None:
        """
        Koristeći Matplotlib prikazati sliku koja je predana kao parametar.
        Ova funkcija ne vraća ništa.
        """
        plt.imshow(image)
        plt.show()

    @staticmethod
    def save_image(image: np.ndarray, path: str) -> None:
        """
        Ova funkcija pohranjuje sliku <image> na disk s imenom koji smo predali
        kao parametar path.
        """
        img_into_pil = Image.fromarray(image)
        img_into_pil.save(path)

    @staticmethod
    def get_red_channel_values(image: np.ndarray) -> np.ndarray:
        """
        Postaviti vrijednosti G i B kanala na nulu.
        Ova funkcija vraća RGB sliku čije su vrijednosti G i B kanala postavljeni na nulu.
        """
        red_channel = image.copy()
        red_channel[:, :, 1] = 0 
        red_channel[:, :, 2] = 0  
        return red_channel


    @staticmethod
    def crop_top_left(image: np.ndarray, height: int, width: int) -> np.ndarray:
        """
        Potrebno je iz ulazne slike <image> izdvojiti gornji-lijevi dio slike veličine height x width.
        Ova funkcija vraća gornji lijevi dio slike image.
        """
        return image[0:height, 0:width]



    @staticmethod
    def center_crop(image: np.ndarray, height: int, width: int) -> np.ndarray:
        """
        Slično kao u prethodnoj funkciji, potrebno je izdvojiti dio slike veličine height x width, ali
        u ovoj funkciji izdvajamo sredinu slike.
        """
        center_y = image.shape[0] // 2
        center_x = image.shape[1] // 2

        half_h = height//2
        half_w = width//2

        return image[center_y - half_w : center_y + half_w, center_x - half_h : center_x + half_h]
 


    @staticmethod
    def stack_channels(red_channel_values: np.ndarray, green_channel_values: np.ndarray,
                       blue_channel_values: np.ndarray) -> np.ndarray:
        """
        Ova funkcija kao parametre prima 3 različite slike koje sadrže vrijednosti R, G i B kanala.
        Veličina ulaznih parametara je (H, W).Potrebno je stvoriti RGB sliku veličine (H, W, 3) koja
        će sadržavati R, G i B vrijesnoti predanih slika.

        Koristite funkcije:
            - np.expand_dims
            - np.concatenate

        Testirajte implementaciju ove funckije korištenjem slika
            - red_channel_values.jpg
            - green_channel_values.jpg
            - blue_channel_values.jpg
        """

    @staticmethod
    def resize_image_to_twice_smaller(image: np.ndarray) -> np.ndarray:
        """
        Ulaznu sliku image veličine (H, W, 3) dvostruko smanjite. Veličina slike koju će
        vratiti ova funckija mora biti (H / 2, W / 2, 3). Zbog jednostavnosti, prilikom
        smanjivanja slike izostavite svaki parni piksel.
        """
