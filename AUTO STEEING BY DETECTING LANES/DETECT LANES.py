import cv2 as cv2
import numpy as np
from MOTOR_DRIVE import *
import time
import math
from StackImages import *
from UTILITIES import *

LEFT_LINE_MAX = -34
LEFT_LINE_MIN = -54
RIGHT_LINE_MIN = 44
RIGHT_LINE_MAX = 64

cap = cv2.VideoCapture(0)
while True:
    s, Img = cap.read()          # Read Image file
    #Img = cv2.imread("Right_12_8.JPG")            # Read Image file
    Img = cv2.resize(Img, (320, 240))       # Resize the Image to standard Height and width
    LANE_img = np.copy(Img)                 # Copy Image to Display it in FINAL Step
    Canny_Img = canny(Img)                  # perform CANNY Edge Detection
    img_cropped = Region(Canny_Img)         # Crop the Image the to avoid Detecting Lines from Total View of the CAMERA

    #lines_canny = cv2.HoughLinesP(Canny_Img, 1, np.pi / 180, 30, np.array([]), minLineLength=20,
                                 # maxLineGap=28)          # Detect the Lines from the CANNY Img to display in FINAL Step

    lines_cropped = cv2.HoughLinesP(img_cropped, 1, np.pi / 180, 30, np.array([]), minLineLength=20,
                                    maxLineGap=28)   # Detect the Lines from the Cropped Img to Find ANGLE

    Left_lines, Right_lines = Find_angle(lines_cropped)
    LeftAngleAvg,L_ack = left_angle_avg(Left_lines)
    RightAngleAvg,R_ack = right_angle_avg(Right_lines)
    print(LeftAngleAvg)
    print(RightAngleAvg)
    """
    if(LEFT_LINE_MAX > LeftAngleAvg) and (LeftAngleAvg > LEFT_LINE_MIN) and (RIGHT_LINE_MAX > RightAngleAvg) and (RightAngleAvg > RIGHT_LINE_MIN):
        go_straight()
        print("STRAIGHT")
    elif(LeftAngleAvg < LEFT_LINE_MIN) or (RightAngleAvg>RIGHT_LINE_MAX):
        go_left()
        print("LEFT")
    elif(LeftAngleAvg > LEFT_LINE_MAX) or (RightAngleAvg<RIGHT_LINE_MIN):
        go_right()
        print("RIGHT")
    else:
        pass
    """
    if (L_ack is 1) and (R_ack is 1):
        if(RIGHT_LINE_MAX > RightAngleAvg) and (RightAngleAvg > RIGHT_LINE_MIN) and (LEFT_LINE_MAX > LeftAngleAvg) and (LeftAngleAvg > LEFT_LINE_MIN):
            go_straight()
            print("STRAIGHT")
        elif(RightAngleAvg>RIGHT_LINE_MAX) or (LeftAngleAvg < LEFT_LINE_MIN):
            go_left()
            print("LEFT")
        elif(RightAngleAvg<RIGHT_LINE_MIN) or (LEFT_LINE_MAX < LeftAngleAvg):
            go_right()
            print("RIGHT")
        else:
            stop()
            print("STOP")
    elif R_ack is 0:
        go_left()
        print("LEFT_1")
    elif L_ack is 0:
        go_right()
        print("RIGHT_1")
    else:
        pass
        


    line_img = display_lines_m(LANE_img, lines_cropped)             # Create An Image to display the Detected lines
    Final_img = cv2.addWeighted(LANE_img, 0.8, line_img, 1, 1)    # Combine the Line Image and LANE Image to Display it
    StackedImages = stackImages(([Canny_Img, img_cropped], [line_img, Final_img]), 1)
    cv2.imshow("StackedImg", StackedImages)
    cv2.waitKey(1)
    #break
