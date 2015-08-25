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

        # list consisting of submissions that already proccessed but not emailed
        self.processed = []

        self.subreddits = settings.SUBREDDITS
        self.keywords = settings.KEYWORDS
        self.exclude = settings.EXCLUDE
        self.e = EmailHandler()

    @staticmethod
    def validate():
        try:
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

            for subreddit, keywords_dict in settings.KEYWORDS.items():
                if type(subreddit) != str or type(keywords_dict) != dict:
                    raise error.BotInvalidKeywords('Invalid keywords data structure')
                for attribute, keyword in keywords_dict.items():
                    if type(attribute) != str or type(keyword) != list:
                        raise error.BotInvalidKeywords('Invalid keywords data structure')

            for subreddit, keywords_dict in settings.EXCLUDE.items():
                if type(subreddit) != str or type(keywords_dict) != dict:
                    raise error.BotInvalidExclude('Invalid exclude data structure')
                for attribute, keyword in keywords_dict.items():
                    if type(attribute) != str or type(keyword) != list:
                        raise error.BotInvalidExclude('Invalid exclude data structure')
        except AttributeError:
            print('Missing configuration, please check your settings')
            sys.exit()

    def log_match(self, subreddit, submission):
        print(str(datetime.datetime.now())
              + " Match found in " + subreddit
              + " subreddit, adding result to mail ")
        print((str(datetime.datetime.now()) + ' title : ' + submission.title))
        print((str(datetime.datetime.now()) + ' url : ' + submission.url))

    def has_keyword(self, subreddit, submission):

        # get a dict of attributes and its keywords for current subreddit
        dict_of_keywords = self.keywords[subreddit]

        for attribute, keywords in dict_of_keywords.items():
            submission_attribute_value = getattr(submission, attribute).lower()

            for keyword in keywords:

                # each of submission attribute will be caselowered
                if keyword in submission_attribute_value \
                        and not self.has_exclude(subreddit, submission) == True \
                        and submission.id not in self.processed:
                    try:
                        keywords = "{'" + attribute + "': ['" + keyword + "']}"
                        self.e.add_header(keywords=keywords,
                                          subreddit=subreddit,
                                          exclude=str(self.exclude[subreddit]))
                    except KeyError:
                        keywords = "{'" + attribute + "': ['" + keyword + "']}"
                        self.e.add_header(keywords=keywords,
                                          subreddit=subreddit)
                    return True
            return False

    def has_exclude(self, subreddit, submission):

        try:
            dict_of_keywords = self.exclude[subreddit]
        except KeyError:
            return False

        for attribute, keywords in dict_of_keywords.items():
            submission_attribute_value = getattr(submission, attribute).lower()
            if any(keyword in submission_attribute_value for keyword in keywords) == True:
                return True
        return False

    def process(self, connection):
        r = connection
        for subreddit in self.subreddits:
            subreddit_str = subreddit  # the subreddit string
            subreddit = r.get_subreddit(subreddit)  # this is an object

            try:  # connection error
                submissions = subreddit.get_hot(limit=50)
            except:
                print("Error has occured " + str(sys.exc_info()[0]))
                break

            for submission in submissions:
                has_keyword = self.has_keyword(subreddit=subreddit_str, submission=submission)

                if submission.id not in self.processed and has_keyword:
                    self.log_match(subreddit=subreddit_str, submission=submission)
                    self.e.add_result(submission=submission)
                    self.processed.append(submission.id)

            time.sleep(2)  # sleep between each subreddits

        if not self.e.content:
            print(str(datetime.datetime.now())
                  + " No match found, waiting for next run at "
                  + str(datetime.datetime.now()
                  + datetime.timedelta(seconds=settings.SLEEP)))
        else:
            print(str(datetime.datetime.now()) + ' Sending results to ' + settings.RECEPIENT_EMAIL)
            self.e.send()
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

