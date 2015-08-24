import time
import datetime
from pprint import pprint

import praw
import settings
from emailhandler import EmailHandler


def run():
    emailed = [] # list consisting of submission that already emailed\
    subreddits = settings.SUBREDDITS
    keywords = settings.KEYWORDS
    for subreddit in subreddits:
        if str(subreddit) not in keywords:
            print "KEYWORDS error, either you haven't set it up or there is no keyword for some of the subreddits"
            return

    exclude = settings.EXCLUDE
    keywords_index = 0

    r = praw.Reddit(user_agent=settings.USER_AGENT)

    while True:
        print str(datetime.datetime.now()) + ' starting bot'
        emailhandler = EmailHandler()

        for subreddit in subreddits:
            subreddit_txt = subreddit
            subreddit = r.get_subreddit(subreddit)
            add_subreddit_header = True # add heading for every match found in each subreddit

            for submission in subreddit.get_hot(limit=50):
                title = submission.title.lower()
                try:  # with exclude
                    has_keyword = not any(string in title for string in exclude[subreddit_txt]) \
                                  and any(string in title for string in keywords[subreddit_txt])
                except: # without exclude
                    has_keyword = any(string in title for string in keywords[subreddit_txt])

                if submission.id not in emailed and has_keyword:
                    print str(datetime.datetime.now()) \
                          + " Match found in " + str(subreddit) \
                          + " subreddit, adding result to mail "
                    print(str(datetime.datetime.now()) + ' title : ' + submission.title)
                    print(str(datetime.datetime.now()) + ' url : ' + submission.url)

                    if add_subreddit_header:
                        try:
                            emailhandler.add_result(['<br><h3>Match found in ' + subreddit_txt \
                                                 + ' subreddit with keywords ' + str(keywords[subreddit_txt]) \
                                                 + ' exclude ' + str(exclude[subreddit_txt]) \
                                                 + '</h3><br>'])
                        except:
                            emailhandler.add_result(['<br><h3>Match found in ' + subreddit_txt \
                                                 + ' subreddit with keywords ' + str(keywords[subreddit_txt]) + '</h3><br>'])
                        add_subreddit_header = False

                    emailhandler.add_result([submission.title + '<br>' + submission.url + '<br><br>'])
                    emailed.append(submission.id)
            time.sleep(5)  # sleep between each subreddits

        if not emailhandler.content:
            print str(datetime.datetime.now()) \
                  + " No match found, waiting for next run at " \
                  + str(datetime.datetime.now() \
                  + datetime.timedelta(seconds=settings.SLEEP))
        else:
            print str(datetime.datetime.now()) + ' Sending results to ' + settings.RECEPIENT_EMAIL
            emailhandler.send()
            print str(datetime.datetime.now()) \
                  +' Waiting for next run at ' + str(datetime.datetime.now() \
                  + datetime.timedelta(seconds=settings.SLEEP))
        time.sleep(settings.SLEEP)  # sleep between each run
