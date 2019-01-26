import cv2
import numpy as np

img=cv2.imread('test.jpg')
cv2.imshow('old',img)
print(img.shape)
res = cv2.resize(img,(128,128))
cv2.imshow('new',res)
cv2.imwrite('test.jpg',res)
print(res.shape)
cv2.waitKey(0)

"""def extraeUnaCara(imagen):
    face_cascade = cv2.CascadeClassifier('haarcascade_fcrontalface_alt.xml')
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) > 1:
        print("More than one faces")
        return None
    else:
        for (x,y,w,h) in faces:
            roi = imagen[y:y+h, x:x+w]
            roi = cv2.resize(roi,TARGET_SIZE)
            return roi
    return None

print(extraeUnaCara('test.jpe'))
"""
