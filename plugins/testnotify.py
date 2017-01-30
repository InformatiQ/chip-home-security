class testnotify:
    def __init__(self, alert_message, reset_message):
        self.alert_message = alert_message
        self.reset_message = reset_message

    def alert(self):
        print self.alert_message

    def reset(self):
        print self.reset_message

    def cleanup(self):
        pass
