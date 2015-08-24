# =============================================================================
# ========================USER AGENT===========================================
# please refer to https://github.com/reddit/reddit/wiki/API for valid
# user agent string
#
# EXAMPLE
# =============================================================================
# USER_AGENT = "Simple reddit notifier by /u/myaccount" DONT USE THIS

USER_AGENT = ""

# =============================================================================
# ========================BOT CONFIGURATION====================================
# You must specify a list of subreddits to crawl and its keywords, notice that
# you must use dictionary for the keywords.
# Exclude is optional.
# Sleep specify how long is the delay between each subreddit. Please adhere to
# the reddit API rules
#
# EXAMPLE
# =============================================================================
# SUBREDDITS = ['gamedeals', 'pcmasterrace']
# KEYWORDS = {'gamedeals': ['free', 'giveaway'], 'pcmasterrace': ['free', 'giveaway']}
# EXCLUDE = {'gamedeals': ['drm']}

SUBREDDITS = []
KEYWORDS = {}
EXCLUDE = {}

SLEEP = 18000  # in seconds

# =============================================================================
# ========================EMAIL INFORMATION====================================
# sender email must be a gmail account
#
# EXAMPLE
# =============================================================================
# SENDER_EMAIL = 'my.bot@gmail.com'
# RECEPIENT_EMAIL = 'my.bot@gmail.com'
# SUBJECT = 'simple reddit notifier'

SENDER_EMAIL = ''
RECEPIENT_EMAIL = ''
SUBJECT = ''
