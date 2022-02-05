import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from PIL import ImageGrab

path = 'Student_Images'
images = []
classNames = []
myList = os.listdir(path)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def Encodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def Attendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')


def captureScreen(bbox=(300,300,690+300,530+300)):
    capScr = np.array(ImageGrab.grab(bbox))
    capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
    return capScr

ListKnown = Encodings(images)
print('Encoding Complete')

img = captureScreen()
imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
fFrame = face_recognition.face_locations(imgS)
eFrame = face_recognition.face_encodings(imgS, fFrame)

for encodeFace, faceLoc in zip(eFrame, fFrame):
   matches = face_recognition.compare_faces(ListKnown, encodeFace)
   faceDis = face_recognition.face_distance(ListKnown, encodeFace)
   Index = np.argmin(faceDis)

   if matches[Index]:
       name = classNames[Index].upper()
       y1, x2, y2, x1 = faceLoc
       y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
       cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
       cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
       cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
       Attendance(name)

cv2.waitKey(0)

