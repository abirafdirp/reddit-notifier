import time
import datetime
import sys
import re

import praw
import settings
import error
from emailhandler import EmailHandler


class Bot:
    def __init__(self):
        # list consisting of submissions that already emailed
        self.emailed = []

        self.subreddits = settings.SUBREDDITS
        self.keywords = settings.KEYWORDS
        self.exclude = settings.EXCLUDE

    @staticmethod
    def validate():
        if not bool(re.search('@gmail.com', settings.SENDER_EMAIL)):
            raise error.BotInvalidSenderEmail

        if not bool(re.search('@', settings.RECEPIENT_EMAIL)):
            raise error.BotInvalidRecepientEmail

        for subreddit in settings.SUBREDDITS:
            if str(subreddit) not in settings.KEYWORDS:
                raise error.BotInvalidKeywords('Missing subreddit in keywords')

        if type(settings.SLEEP) != int:
            raise error.BotInvalidSleep

        if type(settings.KEYWORDS) != dict:
            raise error.BotInvalidKeywords('Invalid keywords data structure')

        if type(settings.EXCLUDE) != dict:
            raise error.BotInvalidExclude

        for subreddit, attributes_list in settings.KEYWORDS.items():
            if type(subreddit) != str or type(attributes_list) != list:
                raise error.BotInvalidKeywords('Invalid keywords data structure')
            for attribute in attributes_list:
                for attribute_name, keywords in attribute.items():
                    if type(attribute_name) != str or type(keywords) != list:
                        raise error.BotInvalidKeywords('Invalid keywords data structure')
                    for keyword in keywords:
                        if type(keyword) != str:
                            raise error.BotInvalidKeywords('Invalid keywords data structure')

        for subreddit, attributes_list in settings.EXCLUDE.items():
            if type(subreddit) != str or type(attributes_list) != list:
                raise error.BotInvalidExclude('Invalid exclude data structure')
            for attribute in attributes_list:
                for attribute_name, keywords in attribute.items():
                    if type(attribute_name) != str or type(keywords) != list:
                        raise error.BotInvalidExclude('Invalid exclude data structure')
                    for keyword in keywords:
                        if type(keyword) != str:
                            raise error.BotInvalidExclude('Invalid exclude data structure')

    def add_header(self, render, attribute, emailhandler, subreddit):
        e = emailhandler
        if render:
            try:
                e.add_result(['<br><h3>Match found in ' + subreddit \
                             + ' subreddit with keywords ' + str(self.keywords[subreddit]) \
                             + ' exclude ' \
                             + str(self.exclude[subreddit]) \
                             + '</h3><br>'])
            except:
                e.add_result(['<br><h3>Match found in ' + subreddit \
                             + ' subreddit with keywords ' \
                             + str(self.keywords[subreddit]) + '</h3><br>'])

    def add_result(self, emailhandler, submission):
        e = emailhandler
        e.add_result([submission.title + '<br>' + submission.url + '<br><br>'])

    def log_match(self, subreddit, submission):
        print(str(datetime.datetime.now())
              + " Match found in " + subreddit
              + " subreddit, adding result to mail ")
        print((str(datetime.datetime.now()) + ' title : ' + submission.title))
        print((str(datetime.datetime.now()) + ' url : ' + submission.url))

    def has_keyword(self, subreddit, submission):

        # get a list of dict of attributes and its keywords for current subreddit
        attributes = self.keywords[subreddit]

        # iterate over each dict of attributes and its keywords
        for attribute in attributes:

            # because the keywords are inside a list, so we need to get the
            # value of them via its key
            for key in attribute:

                # each of submission attribute will be caselowered
                sub_attribute = getattr(submission, key).lower()

                return any(value in sub_attribute for value in attribute[key]) \
                       and not self.has_exclude(subreddit=subreddit, submission=submission)

    def has_exclude(self, subreddit, submission):

        try:
            attributes = self.exclude[subreddit]
        except KeyError:
            return False

        for attribute in attributes:
            for key in attribute:
                sub_attribute = getattr(submission, key).lower()
                return any(keyword in sub_attribute for keyword in attribute[key])

    def process(self, connection):
        r = connection
        e = EmailHandler()
        for subreddit in self.subreddits:
            subreddit_str = subreddit  # the subreddit string
            subreddit = r.get_subreddit(subreddit)  # this is an object

            # add heading for each subreddit
            add_subreddit_header = True

            try:  # connection error
                submissions = subreddit.get_hot(limit=50)
            except:
                print("Error has occured " + str(sys.exc_info()[0]))
                break

            for submission in submissions:
                has_keyword = self.has_keyword(subreddit=subreddit_str, submission=submission)

                if submission.id not in self.emailed and has_keyword:
                    self.log_match(subreddit=subreddit_str, submission=submission)

                    self.add_header(add_subreddit_header, emailhandler=e,
                                    subreddit=subreddit_str)
                    add_subreddit_header = False

                    self.add_result(emailhandler=e, submission=submission)
                    self.emailed.append(submission.id)

            time.sleep(2)  # sleep between each subreddits

        if not e.content:
            print(str(datetime.datetime.now())
                  + " No match found, waiting for next run at "
                  + str(datetime.datetime.now()
                  + datetime.timedelta(seconds=settings.SLEEP)))
        else:
            print(str(datetime.datetime.now()) + ' Sending results to ' + settings.RECEPIENT_EMAIL)
            e.send()
            print(str(datetime.datetime.now())
                  +' Waiting for next run at ' + str(datetime.datetime.now()
                  + datetime.timedelta(seconds=settings.SLEEP)))

    def run(self):
        while True:
            try:  # connection error
                r = praw.Reddit(user_agent=settings.USER_AGENT)
            except:
                print("Error has occured " + str(sys.exc_info()[0]))
                break
            print(str(datetime.datetime.now()) + ' Starting bot')
            self.process(connection=r)
            time.sleep(settings.SLEEP)  # sleep between each run

