import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

while True:
    GPIO.output(4, GPIO.HIGH)
    GPIO.output(5, GPIO.LOW)
    time.sleep(1)
    GPIO.output(4, GPIO.LOW)
    GPIO.output(5, GPIO.HIGH)
    time.sleep(1)