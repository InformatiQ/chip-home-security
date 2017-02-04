import smtplib
import datetime
from email.MIMEMultipart import MIMEMultipart

class mailnotify:
    def __init__(self, host, username, password, frommail='chip@home', tomail):
        self.smtp = smtplib.SMTP(host, port)
        server.starttls()
        server.login(username, password)
        self.msg = MIMEMultipart()
        self.frommail = frommail
        self.tomail = tomail
        self.msg['From'] = frommail
        self.msg['To'] = tomail

    def alert(self):
        self.msg['Subject'] = 'Intruder alert'
        body = "motion detected at your home at %s" %(datetime.datetime.now())
        self.smtp.sendmail(self.msg['From'], [self.msg['To']], self.msg.as_string())

    def reset(self):
        self.msg['Subject'] = 'Intruder alert OVER'
        body = "alert acknoleged at %s" %(datetime.datetime.now())
        self.smtp.sendmail(self.msg['From'], [self.msg['To']], msg.as_string())

    def cleanup(self):
        self.smtp.quit()
