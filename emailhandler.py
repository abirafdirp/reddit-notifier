import yagmail
import settings


class EmailHandler:

    def __init__(self):
        recepient = settings.RECEPIENT_EMAIL
        content = []

    @staticmethod
    def register(self):
        print "Provide your email information below, password is stored in the system keyring (safe)"
        username = input('username : ')
        password = input('password : ')
        yagmail.register(username, password)

    def add_result(self, result):
        self.content += result

    def send(self):
        yagmail.SMTP(settings.SENDER_EMAIL).send(settings.RECEPIENT_EMAIL,settings.SUBJECT, self.content)



