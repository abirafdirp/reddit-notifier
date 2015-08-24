import time
import datetime
import sys

import praw
import settings
from emailhandler import EmailHandler


def run():

    # list consisting of submissions that already emailed
    emailed = []

    subreddits = settings.SUBREDDITS
    keywords = settings.KEYWORDS
    exclude = settings.EXCLUDE

    for subreddit in subreddits:
        if str(subreddit) not in keywords:
            print("KEYWORDS error, either you haven't set it up or there is no keyword for some of the subreddits")
            return

    if type(settings.SLEEP) != int:
        print('Invalid sleep settings')
        return

    while True:

        # try is put here because the statements that may raised connection error
        # exception is too spread out in this block. This also used for catching
        # bad settings configuration
        try:
            r = praw.Reddit(user_agent=settings.USER_AGENT)
            print(str(datetime.datetime.now()) + ' Starting bot')
            emailhandler = EmailHandler()

            for subreddit in subreddits:
                subreddit_txt = subreddit
                subreddit = r.get_subreddit(subreddit)

                # add heading for every match found in each subreddit
                add_subreddit_header = True

                for submission in subreddit.get_hot(limit=50):
                    title = submission.title.lower()
                    try:  # with exclude
                        has_keyword = not any(string in title for string in exclude[subreddit_txt]) \
                                      and any(string in title for string in keywords[subreddit_txt])
                    except:  # without exclude
                        has_keyword = any(string in title for string in keywords[subreddit_txt])

                    if submission.id not in emailed and has_keyword:
                        print(str(datetime.datetime.now()) \
                              + " Match found in " + str(subreddit) \
                              + " subreddit, adding result to mail ")
                        print((str(datetime.datetime.now()) + ' title : ' + submission.title))
                        print((str(datetime.datetime.now()) + ' url : ' + submission.url))

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
                print(str(datetime.datetime.now()) \
                      + " No match found, waiting for next run at " \
                      + str(datetime.datetime.now() \
                      + datetime.timedelta(seconds=settings.SLEEP)))
            else:
                print(str(datetime.datetime.now()) + ' Sending results to ' + settings.RECEPIENT_EMAIL)
                emailhandler.send()
                print(str(datetime.datetime.now()) \
                      +' Waiting for next run at ' + str(datetime.datetime.now() \
                      + datetime.timedelta(seconds=settings.SLEEP)))
            time.sleep(settings.SLEEP)  # sleep between each run
        except KeyboardInterrupt:
            return
        except:
            print("Error has occured, most likely bad settings configuration or unable to contact reddit. Error message " + str(sys.exc_info()[0]))
