import cv2
import numpy as py
import face_recognition as fa
import os

path = 'Student_Images'
images = []
Names = []
List = os.listdir(path)
print(List)
for cl in List:
    img3 = cv2.imread(f'{path}/{cl}')
    images.append(img3)
    Names.append(os.path.spittext(cl)[0])

def FE(images):
    el = []
    for im in images:
        im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
        en = fa.face_encodings(im)[0]
        el.append(en)
    return el

elk = FE(images)
