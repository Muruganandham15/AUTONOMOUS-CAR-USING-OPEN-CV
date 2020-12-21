# AUTONOMOUS-RC-CAR-BY-DETECTING-LANES
Detect Lanes Real time and Tilt steering accordingly using RASPBERRY-PI
![WhatsApp Image 2020-12-18 at 5 57 10 PM](https://user-images.githubusercontent.com/66992192/102755535-ebd7e880-43b1-11eb-854b-590ccba3adb8.jpeg)

**STEP 1:  CAPTURE IMAGE**
->Capture Image from the Real time video from RASPBERRY-PI CAM
->This is a continous process that happens every 50ms

![IMG](https://user-images.githubusercontent.com/66992192/101622808-dd590b00-3a5a-11eb-864e-0e019c053d6a.jpg)

**STEP 2: CANNY EDGE IMAGE**
->Covert the Captured Image to Gray scale Image,
->Using Canny Edge Detection Technique,Detect the lines from the Gray scale Image.
Note: Thresholds used in edge detection depends on Environment

![canny](https://user-images.githubusercontent.com/66992192/101622695-ba2e5b80-3a5a-11eb-9df6-379799a943d9.jpg)

**STEP 3: REGION OF INTEREST**
->From the CANNY Image ,Crop the Image According to the Region of Interest
![CROPPED](https://user-images.githubusercontent.com/66992192/101623862-61f85900-3a5c-11eb-9311-606a658eb1fa.jpg)

**STEP 4: HOUGH LINES**
->From Cropped Image,Find Hough lines Here the BIN Threshold changes with environment,The result of the image is used to TILT RC CAR
->From Canny Image,Find Hough lines,The result of the image is used to Display the OVERALL view of the CAMERA.

**STEP 5: FIND ANGLE**
->Form Hough lines detected with cropped image,Seperate the Lines as LEFT LANES and RIGHT LANES by finding slope of each line
->Find the average angle of LEFT LANE and RIGHT LANE

![Find_angle](https://user-images.githubusercontent.com/66992192/101622160-0af18480-3a5a-11eb-8823-5c1c66c89610.png)

**STEP 6: STEER RC CAR**
->By Comparing the Threshold for LEFT LANE ANGLE and RIGHT LANE ANGLE,The car is tilted to LEFT ,RIGHT or To go STRAIGHT

![FIANL](https://user-images.githubusercontent.com/66992192/101623478-d7aff500-3a5b-11eb-9d61-dc8ec4b55bee.jpg)
