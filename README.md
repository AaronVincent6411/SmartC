# SmartC
### _A Complete Solution for Educational Institutions_

## Introduction

![Logo](Images/SmartC_Logo.png)

### SmartC is a platform for educational institutions for accessing and providing effective way of management to students and teachers of a campus

## Basic Features

- [x] Automated attendance collection

- [x] Face detection during online sessions

- [x] Access to student data

- [x] 24X7 helpdesk

## Advantages

- Ensure students attending online

- Ease access to student data

- Easy to collect attendance

## Library Prerequisites

  ### opencv library
  `pip install opencv-python`

  ### dlib library
   Before installing dlib ensure cmake 

   `pip install dlib`

   Build the main dlib library
   ```
   cd dlib
   mkdir build
   cd build
   cmake ..
   cmake --build .
   ```
   Build and install the Python extensions:

   `cd ..`
   `python3 setup.py install`
 
  ### face recognition library
   `pip3 install face_recognition`
