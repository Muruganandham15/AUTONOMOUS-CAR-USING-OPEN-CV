import cv2 as cv2
import numpy as np
from MOTOR_DRIVE import *
import time
import math
from UTILITIES import *

cap = cv2.VideoCapture(0)
while True:
    s, img = cap.read()
    cv2.imshow("A",img)
    cv2.imwrite("/home/pi/Desktop/AUTO STEEING BY DETECTING LANES/REF.JPG",img)
    break



