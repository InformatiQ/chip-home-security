import os, time
import CHIP_IO.GPIO as GPIO
import threading

class MotionDetect(threading.Thread):
    def __init__(self, pin):
        GPIO.setup(pin, GPIO.IN)

    def detect(self):
        global Detected
        if GPIO.input("XIO-P0"):
            Detected = True

    def reset(self):
        global Detected
        Detected = False

GPIO.setup("XIO-P1", GPIO.OUT)
def alert():
    print "ON"
    GPIO.output("XIO-P1", 0)

def reset():
    print "OFF"
    GPIO.output("XIO-P1", 1)


if __name__ == "__main__":
    try:
        Detected = False
        motion = MotionDetect('XIO-P0')
        motion.detect()
        if Detected:
            alert

    except:
        GPIO.cleanup()
