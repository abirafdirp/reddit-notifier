import sys
import datetime
import getpass

import keyring
import yagmail
import settings


class EmailHandler:

    def __init__(self):
        self.recepient = settings.RECEPIENT_EMAIL
        self.content = []

    @staticmethod
    def register():
        print("Provide your email password below. Password is stored in the system keyring (safe)")
        password = getpass.getpass('password : ')
        password2 = getpass.getpass('confirm password : ')
        if password != password2:
            print('Password does not match')
            sys.exit()
        keyring.set_password('yagmail', settings.SENDER_EMAIL, password)

    def add_header(self, keywords, subreddit, exclude=''):
        if exclude != '':
            self.content += ['<br><h3>Match found in ' + subreddit \
                         + ' subreddit with keywords ' + keywords \
                         + ' exclude ' \
                         + exclude \
                         + '</h3><br>']
        else:
            self.content += ['<br><h3>Match found in ' + subreddit \
                         + ' subreddit with keywords ' \
                         + keywords + '</h3><br>']

    def add_header_keywords(self, keywords):
        pass

    def add_header_exclude(self, exclude):
        pass

    def add_result(self, submission):
        self.content += [submission.title + '<br>' + submission.url + '<br><br>']

    def send(self):
        try:
            yagmail.SMTP(settings.SENDER_EMAIL).send(settings.RECEPIENT_EMAIL, settings.SUBJECT, self.content)
            print(str(datetime.datetime.now()) + ' Email sent')
            self.content = []
        except not KeyboardInterrupt:
            print(str(datetime.datetime.now()) +
                  'Error occured, email not sent, error message ' +
                  str(sys.exc_info()[0]))
            print(str(datetime.datetime.now()) +
                  'Results will be emailed at next run')





