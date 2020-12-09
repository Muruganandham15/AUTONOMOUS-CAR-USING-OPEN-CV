import RPi.GPIO as GPIO

STRAIGHT = 4
LEFT = 17
RIGHT = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)
GPIO.setup(STRAIGHT, GPIO.OUT)
GPIO.setup(LEFT, GPIO.OUT)
GPIO.setup(RIGHT, GPIO.OUT)


def motor_parameters(s, ll, r):
    GPIO.output(STRAIGHT, s)
    GPIO.output(LEFT, ll)
    GPIO.output(RIGHT, r)


def go_left():
    motor_parameters(0, 1, 0)


def go_right():
    motor_parameters(0, 0, 1)


def go_straight():
    motor_parameters(1, 0, 0)
