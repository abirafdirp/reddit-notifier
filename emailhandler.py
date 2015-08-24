import sys
import datetime

import keyring
import yagmail
import settings


class EmailHandler:

    def __init__(self):
        self.recepient = settings.RECEPIENT_EMAIL
        self.content = []

    @staticmethod
    def register():
        print "Provide your password information below, password is stored in the system keyring (safe)"
        password = raw_input('password : ')
        keyring.set_password('yagmail', settings.SENDER_EMAIL, password)

    def add_result(self, result):
        self.content += result

    def send(self):
        try:
            yagmail.SMTP(settings.SENDER_EMAIL).send(settings.RECEPIENT_EMAIL, settings.SUBJECT, self.content)
            print str(datetime.datetime.now()) + ' Email sent'
        except:
            print 'Error occured, email not sent, error code ' + sys.exc_info()[0]



