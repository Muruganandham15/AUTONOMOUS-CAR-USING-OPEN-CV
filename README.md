# AUTONOMOUS-RC-CAR-BY-DETECTING-LANES
Detect Lanes Real time and Tilt steering accordingly using RASPBERRY-PI

STEP 1: CAPTURE IMAGE
->Capture Image from the Real time video from RASPBERRY-PI CAM
->This is a continous process that happens every 50ms

STEP 2: CANNY EDGE IMAGE
->Covert the Captured Image to Gray scale Image,
->Using Canny Edge Detection Technique,Detect the lines from the Gray scale Image.
Note: Thresholds used in edge detection depends on Environment

STEP 3: REGION OF INTEREST
->From the CANNY Image ,Crop the Image According to the Region of Interest

STEP 4: HOUGH LINES
->From Cropped Image,Find Hough lines Here the BIN Threshold changes with environment,The result of the image is used to TILT RC CAR
->From Canny Image,Find Hough lines,The result of the image is used to Display the OVERALL view of the CAMERA.

STEP 5: FIND ANGLE
->Form Hough lines detected with cropped image,Seperate the Lines as LEFT LANES and RIGHT LANES by finding slope of each line
->Find the average angle of LEFT LANE and RIGHT LANE

STEP 6: STEER RC CAR
->By Comparing the Threshold for LEFT LANE ANGLE and RIGHT LANE ANGLE,The car is tilted to LEFT ,RIGHT or To go STRAIGHT

![REF2](https://user-images.githubusercontent.com/66992192/101620640-22c80900-3a58-11eb-836b-ca7dc489f240.jpg)
