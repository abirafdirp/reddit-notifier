import sys
import datetime
import getpass
import re

import keyring
import yagmail
import settings


class EmailHandler:

    def __init__(self):
        self.recepient = settings.RECEPIENT_EMAIL
        self.content = []

    @staticmethod
    def register():
        if not bool(re.search('@gmail.com', settings.SENDER_EMAIL)):
            print('Invalid sender email address, please refer to docs')
            sys.exit()
        print("Provide your email password information below, password is stored in the system keyring (safe)")
        password = getpass.getpass('password : ')
        keyring.set_password('yagmail', settings.SENDER_EMAIL, password)

    def add_result(self, result):
        self.content += result

    def send(self):
        try:
            yagmail.SMTP(settings.SENDER_EMAIL).send(settings.RECEPIENT_EMAIL, settings.SUBJECT, self.content)
            print(str(datetime.datetime.now()) + ' Email sent')
        except:
            print('Error occured, email not sent, error message ' + str(sys.exc_info()[0]))



