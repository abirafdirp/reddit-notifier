import time
import datetime
import sys

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

    def validate(self):
        for subreddit in self.subreddits:
            if str(subreddit) not in self.keywords:
                raise error.BotInvalidSettings

        if type(settings.SLEEP) != int:
            raise error.BotInvalidSettings

    def add_header(self, render, emailhandler, subreddit):
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
                title = submission.title.lower()
                try:  # with exclude
                    has_keyword = not any(string in title for string in self.exclude[subreddit_str]) \
                                  and any(string in title for string in self.keywords[subreddit_str])
                except:  # without exclude
                    has_keyword = any(string in title for string in self.keywords[subreddit_str])

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

