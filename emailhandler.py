import sys
import datetime

import yagmail
import settings


class EmailHandler:

    def __init__(self):
        self.recepient = settings.RECEPIENT_EMAIL
        self.content = []

    @staticmethod
    def register():
        print "Provide your sender email information below, password is stored in the system keyring (safe)"
        username = raw_input('username : ')
        password = raw_input('password : ')
        yagmail.register(username, password)

    def add_result(self, result):
        self.content += result

    def send(self):
        try:
            yagmail.SMTP(settings.SENDER_EMAIL).send(settings.RECEPIENT_EMAIL,settings.SUBJECT, self.content)
            print str(datetime.datetime.now()) + ' Email sent'
        except:
            print 'Error occured, email not sent, error code ' + sys.exc_info()[0]



