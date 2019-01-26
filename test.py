mport numpy as np
from keras.models import Model, load_model
import csv

#load model and prediction dataset
model = load_model('model.h5')

#make predictions
preds = model.predict(test_input,verbose=1)
preds = np.argmax(preds,axis=1)
print(preds.shape)

#write the predictions into a csv file
counter = 1
with open("answer.csv", "w",newline='') as file:
    header = ['ImageId','Label']
    writer = csv.DictWriter(file,delimiter=',',fieldnames = header)
    writer.writeheader()
    for rows in preds:
        writer.writerow({'ImageId' : counter,'Label' : rows})
        counter += 1
