#import all necessary libraries
import numpy as np
import h5py
import cv2
import keras
from keras.models import Model, load_model

model = load_model('ResNet50.h5')
#load test set labeled pairs
X_test = np.load('dataset/X_test.npy')
Y_test = np.load('dataset/Y_test.npy')

TestAccuracy = model.evaluate(X_CV, Y_CV)
print ("Loss = " + str(preds[0]))
print ("Test Accuracy = " + str(preds[1]))
model.summary
