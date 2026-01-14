from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from MyComputerVision import MyComputerVision as mcv


"""
1. zadatak
Pomoću PIL biblioteke učitajte sliku “houses.jpg”. Prikažite sliku u RGB formatu u koja prikazuje samo intenzitet zelenih vrijednosti.
Konačan prikaz treba izgledati kao sljedeća slika:
"""

image = Image.open("img/houses.jpg")
print(f"Tip objekta: {type(image)}")

image_numpy = np.asarray(image)
green_image = np.zeros_like(image_numpy)
green_image[:, :, 1] = image_numpy[:, :, 1]

#plt.imshow(green_image)
#plt.show()


"""
2. Zadatak
Koristeći Numpy stvorite sliku veličine 500x500. Postavite vrijednosti polja tako da slika prikazuje crvenu boju kao na sljedećoj slici. 
Prikažite sliku. Rezultat bi trebao izgledati kao na sljedećoj slici: 
Stvorite novu sliku istih dimenzija, ali zelene boje. Kada bi zbrojili te dvije slike, koja boja trebala biti prikazana? Prikažite rezultat zbrajanja
"""

red = np.zeros([500, 500, 3], dtype=np.uint8)
#print(red)
red[:, :, 0] = 255
#print(red)

# plt.imshow(red)
# plt.show()

# green = np.zeros([500, 500, 3], dtype=np.uint8)
# green[:, :,  1] = 255
# plt.imshow(green)
# plt.show()

# new_color = red + green #yellow
# plt.imshow(new_color)
# plt.show()



"""
3. Zadatak

Učitajte slike “AI_Lipik_1.jpg” i “AI_Lipik_2.jpg”. Odgovarajućom Numpy funkcijom spojite 
navedene dvije slike po širini, te prikažite rezultat kao na sljedećoj slici:
"""

lipik_1 = Image.open("img/AI_Lipik_1.jpg")
lipik_2 = Image.open("img/AI_Lipik_2.jpg")

lipik_1_numpy = np.asarray(lipik_1)
lipik_2_numpy = np.asarray(lipik_2)

#print(lipik_1_numpy.shape)
#print(lipik_2_numpy.shape)

final_image = np.zeros([lipik_1_numpy.shape[0], lipik_1_numpy.shape[1] * 2, 3], dtype=np.uint8)
#print(final_image)

final_image = np.concatenate([lipik_1_numpy, lipik_2_numpy], axis=1)

plt.imshow(final_image)
plt.show()



"""
4. Zadatak
"""

#load image
image_house_array = mcv.load_image("img/houses.jpg")

#convert to red channel
red_image = mcv.get_red_channel_values(image_house_array)
#mcv.show_image(red_image)

#crop top letf corner
crop_top_left = mcv.crop_top_left(image_house_array, 250, 350)
#mcv.show_image(image_house_array)
#mcv.show_image(crop_top_left)

#crop center
cropped_center = mcv.center_crop(image_house_array, 400, 200)
mcv.show_image(cropped_center)