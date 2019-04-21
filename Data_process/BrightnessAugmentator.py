import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np
import cv2
import os
from PIL import Image, ImageEnhance
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

#image = 'test.png'

folder = "test" #target folder
onlyfiles = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
#define train files
train_files = []
i=0
for _file in onlyfiles:
    train_files.append(_file)

print("Files in train_files: %d" % len(train_files))

channels = 3
image_height = 128
image_width = 128


for _file in train_files:
    try:
        img = Image.open(folder + "/" + _file)  # this is a PIL image
        # Convert to Numpy Array
        enhancer = ImageEnhance.Brightness(img)
        enhanced_im = enhancer.enhance(1.5)#0.5
        enhanced_im.save("test2/{}_brightnessUp.png".format(i)) #output directory 
        i += 1

    except(ValueError,OSError):
        pass

print("All images brightness augmentated up!")
