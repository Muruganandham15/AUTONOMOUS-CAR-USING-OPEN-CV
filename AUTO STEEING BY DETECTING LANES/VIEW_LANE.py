import cv2 as cv2
import numpy as np
from MOTOR_DRIVE import *
import time
import math
from UTILITIES import *

cap = cv2.VideoCapture(0)
while True:
    s, img = cap.read()
    img=cv2.flip(img,1)
    cv2.imshow("A",img)
    cv2.waitKey(1)



