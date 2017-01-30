import CHIP_IO.GPIO as GPIO

class lednotify:
    def __init__(self, IO):
        self.IO = IO
        GPIO.setup(self.IO, GPIO.OUT)

    def alert(self):
        GPIO.output(self.IO, 0)

    def reset(self):
        GPIO.output(self.IO, 1)

    def cleanup():
        GPIO.cleanup(self.IO)
