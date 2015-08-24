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

Below are the configurations that you need to specified in the settings.py

======================================= ===================================================== ============================================== 
SETTINGS                                 Explanation                                          Example                           
======================================= ===================================================== ============================================== 
USER_AGENT                              https://github.com/reddit/reddit/wiki/API               USER_AGENT = "Simple reddit notifier by /u/myaccount" DONT USE THIS
SUBREDDITS                              list of subreddits                                      SUBREDDITS = ['gamedeals', 'pcmasterrace']                                     
KEYWORDS                                dictionary of subreddits with list of keywords in it                               KEYWORDS = {'gamedeals': ['free', 'giveaway'], 'pcmasterrace': ['free', 'giveaway']}                                       
EXCLUDE                                 (OPTIONAL)                                              EXCLUDE = {'gamedeals': ['drm']}   
SLEEP                                   delay between runs in seconds                           SLEEP = 18000 
SENDER_EMAIL                            a valid gmail account name with @gmail.com
RECEPIENT_EMAIL                         a valid email address
SUBJECT                                 email subject
======================================= ===================================================== ============================================== 

Exclude is sometimes useful e.g. a free game notifier script that has free in its keywords will catch "DRM free" submission, so you include the DRM in the exclude dictionary. 

TODO
-------------

Match other attribute other than title (configurable)