import time
import datetime
from pprint import pprint

import praw
import settings
from emailhandler import EmailHandler


def run():
    checked = []
    keywords = settings.KEYWORDS
    keywords_index = 0

    print str(datetime.datetime.now()) + ' starting bot'
    r = praw.Reddit(user_agent=settings.USER_AGENT)

    while True:
        emailhandler = EmailHandler()

        for subreddit in settings.SUBREDDITS:
            subreddit = r.get_subreddit(subreddit)
            add_subreddit_header = True # add heading for every match found in each subreddit

            for submission in subreddit.get_hot(limit=50):
                title = submission.title.lower()
                has_keyword = any(string in title for string in keywords[keywords_index])

                if submission.id not in checked and has_keyword:
                    print str(datetime.datetime.now()) \
                          + " Match found in " + str(subreddit) \
                          + " subreddit, adding result to mail "
                    print(str(datetime.datetime.now()) + ' title : ' + submission.title)
                    print(str(datetime.datetime.now()) + ' url : ' + submission.url)

                    if add_subreddit_header:
                        emailhandler.add_result(['\nMatch found in ' + str(subreddit) + ' subreddit with keywords ' + keywords[keywords_index] + '\n\n'])
                        add_subreddit_header = False

                    emailhandler.add_result([submission.title + '\n' + submission.url + '\n\n'])
                    checked.append(submission.id)
            time.sleep(5)  # sleep between each subreddits
            keywords_index += 1

        keywords_index = 0

        if emailhandler.content:
            print str(datetime.datetime.now()) + ' Sending results to ' + settings.RECEPIENT_EMAIL
            emailhandler.send()
        else:
            print str(datetime.datetime.now()) \
                  + " No match found, waiting for next run at " \
                  + str(datetime.datetime.now() \
                  + datetime.timedelta(seconds=settings.SLEEP))
        time.sleep(settings.SLEEP)  # sleep between each run
