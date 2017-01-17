import os, sys, time, signal
#import CHIP_IO.GPIO as GPIO
import threading

class MotionDetect(threading.Thread):
    def __init__(self, pin):
        #GPIO.setup(pin, GPIO.IN)
        super(MotionDetect, self).__init__()
        self._stop = threading.Event()

    def run(self):
        print("Detecting motion"),
        while not self._stop.isSet():
            print "thread stop: %s" %self._stop.isSet()
            print("."),
            global Detected
            #if GPIO.input("XIO-P0"):
            #    Detected = True
            if os.path.exists('/tmp/motion'):
                if not Detected:
                    print "motion detected"
                Detected = True
            time.sleep(2)

    def reset(self):
        global Detected
        Detected = False

    def stop(self):
        print "terminating thread"
        self._stop.set()

#GPIO.setup("XIO-P1", GPIO.OUT)
def alert():
    print "ON"
    #GPIO.output("XIO-P1", 0)

def reset():
    print "OFF"
    #GPIO.output("XIO-P1", 1)

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    motion.stop()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def main():
    try:
        Detected = False
        motion = MotionDetect('foo')
        print "start detection"
        motion.start()
        while True:
            print "checking %s" %Detected
            if Detected:
                alert()
            if os.path.exists('/tmp/reset'):
                Detected = False
                reset()
            time.sleep(2)
    except Exception as e:
        print "error -> %s" %str(e)
        motion.stop()
        #GPIO.cleanup()

if __name__ == "__main__":
    main()
