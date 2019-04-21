import numpy as np 
from matplotlib import pyplot as plt

#select the image and show
show_img = (X_train_orig[0]).astype(np.uint8)
print(show_img)
plt.imshow(show_img)
plt.show()
