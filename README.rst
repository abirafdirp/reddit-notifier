reddit-notifier
==============================

A configurable simple script that will notify you through email if a submission title matches with keywords you specified.

Installation
-------------

Clone the repo::
   git clone https://github.com/abirafdirp/reddit-notifier

Install the requirements::
   pip install -r requirements.txt

Run it::
   python run.py


Configuration
-------------

Below are the configurations that you need specified in the settings.py

======================================= ================================================ ============================================== 
SETTINGS                                 Explanation                                      Example                           
======================================= ================================================ ============================================== 
USER_AGENT                              https://github.com/reddit/reddit/wiki/API         USER_AGENT = "Simple reddit notifier by /u/myaccount" DONT USE THIS
SUBREDDITS                              list of subreddits                                SUBREDDITS = ['gamedeals', 'pcmasterrace']                                     
KEYWORDS                                dictionary of keywords with its subreddit value                               KEYWORDS = {'gamedeals': ['free', 'giveaway'], 'pcmasterrace': ['free', 'giveaway']}                                       
EXCLUDE                                 (OPTIONAL)                                        EXCLUDE = {'gamedeals': ['drm']}   
SLEEP                                   delay between subreddit in seconds                SLEEP = 18000 
SENDER_EMAIL                            a valid gmail account name with @gmail.com
RECEPIENT_EMAIL                         a valid email address
SUBJECT                                 email subject
======================================= ================================================ ============================================== 

TODO
-------------

Match other attribute other than title (configurable)