import cv2
import numpy as py
import face_recognition as fa

img = fa.load_image_file('Student_Images/Student1.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img2 = fa.load_image_file('Student_Images/Student1.jpg')
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

fl = fa.face_locations(img)[0]
fe = fa.face_encodings(img)[0]
cv2.rectangle(img,(fl[3],fl[0]),(fl[1],fl[2]),(255,0,255),2)

fl2 = fa.face_locations(img2)[0]
fe2 = fa.face_encodings(img2)[0]
cv2.rectangle(img,(fl[3],fl[0]),(fl[1],fl[2]),(255,0,255),2)

det = fa.compare_faces([fe],fe2)
fd = fa.face_distance([fe],fe2)

cv2.imshow('Output',img)
cv2.imshow('Output',img2)
cv2.waitKey(0)
