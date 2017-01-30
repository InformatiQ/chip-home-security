import os, sys, time, signal, getopt
import threading
import json

import web

#Import plugins
sys.path.append("./plugins")
from testnotify import testnotify

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    motion.stop()
    sys.exit(0)


class MotionDetect(threading.Thread):
    def __init__(self, pin):
        #GPIO.setup(pin, GPIO.IN)
        super(MotionDetect, self).__init__()
        self._stop = threading.Event()

    def run(self):
        print("Detecting motion"),
        while not self._stop.isSet():
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


class WebUI(threading.Thread):
    def __init__(self):
        super(WebUI, self).__init__()

    def run (self):
        urls = ('/', 'WebUI')
        app = web.application(urls, globals())
        app.run()

    def GET(self):
        global Enabled
        global Detected
        web.header('Content-Type', 'application/json')
        response = {'enabled': Enabled, 'intruder': Detected}
        return json.dumps(response)

    def POST(self):
        pass

def callback(alerts=[]):
    if type(alerts) != list:
        sys.exit()
    try:
        global Detected
        global Enabled
        while True:
            if Detected and Enabled:
                for a in alerts:
                    a.alert()
            if os.path.exists('/tmp/reset'):
                Detected = False
                for a in alerts:
                    a.reset()
            time.sleep(1)
    except Exception as e:
        print "error -> %s" %str(e)
        motion.stop()
        for a in alerts:
            a.cleanup()
        sys.exit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hw:", ['help', 'web'])
    except getopt.GetoptError:
        print 'alarm.py [-h|--help] [-w _PORT_ |--web=_PORT_]'
        sys.exit(2)
    Detected = False
    Enabled = True
    motion = MotionDetect('foo')
    motion.start()
    print opts
    print args
    #if opts['-w']:
    #  WebUI().start(opts['-w'])
    callback([testnotify("alert1", "reset1"), testnotify('alert2', 'reset2')])
