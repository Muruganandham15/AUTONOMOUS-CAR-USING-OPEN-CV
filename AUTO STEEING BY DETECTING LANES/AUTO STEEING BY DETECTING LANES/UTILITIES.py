import cv2
import numpy as np
import math


def canny(image):
    imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)
    imgCanny = cv2.Canny(imgBlur, 220, 255)
    return imgCanny


def Region(img):
    height=img.shape[0]
    """polygon=np.array([
        [(0,height),(640,height),(640,180),(0,180)]
    ])"""
    polygon = np.array([
        [(0, height), (640, height), (540, 180), (100, 180)]
    ])
    mask = np.zeros_like(img)
    cv2.fillPoly(mask,polygon,(255,255,255))
    img_croped=cv2.bitwise_and(img,mask)
    return img_croped


def display_lines_m(img, lines):
    line_img = np.zeros_like(img)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_img, (x1, y1), (x2, y2), (0, 0, 255), 10)
    return line_img


def Find_angle(lines):
    Left_side=[]
    Right_side=[]
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            parameters = np.polyfit((x1, x2), (y1, y2), 1)
            slope, intercept = parameters
            if slope < 0:
                Left_side.append(line)
            if slope > 0:
                Right_side.append(line)

    return Left_side, Right_side


def right_angle_avg(lines):
    r_angle = []
    for i in range(len(lines)):
        x1, y1, x2, y2 = lines[i][0]
        angle = math.atan2(y2 - y1, x2 - x1)
        angle = (angle * 180) / np.pi
        r_angle.append(angle)
    avg = np.average(r_angle)
    return avg


def left_angle_avg(lines):
    l_angle = []
    for i in range(len(lines)):
        x1, y1, x2, y2 = lines[i][0]
        angle = math.atan2(y2 - y1, x2 - x1)
        angle = (angle * 180) / np.pi
        l_angle.append(angle)
    avg = np.average(l_angle)
    return avg


def empty(a):
    pass

