#This is a file that displays images that are stored numpy arrays form in a single 
#page with customed row and column size and number of images you want to display

import numpy as np
from matplotlib import pyplot as plt

def display_numpyImages(images, col_size, row_size):
    counter = 826
    fig, ax = plt.subplots(row_size, col_size, figsize=(row_size*2.5,col_size*1.5))
    for row in range(0,row_size):
        for col in range(0,col_size):
            try:
                ax[row][col].imshow(images[counter, :, :, :])
                counter += 1
            except(IndexError):
                pass
X_CVTest = np.load('X_CVTest.npy')
X_CVTest /= 255.
display_numpyImages(X_CVTest,10,10)
plt.show()
