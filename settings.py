# Please refer to the docs https://github.com/abirafdirp/reddit-notifier
# complete explanation
#
# =============================================================================
# ================================USER AGENT===================================
# USER_AGENT = "Simple reddit notifier 0.1 by /u/blah"

USER_AGENT = ''
# =============================================================================
# =============================BOT CONFIGURATION===============================
# SUBREDDITS = ['gamedeals', 'pcmasterrace', 'netsec', 'starcitizen']
# KEYWORDS = {'gamedeals': {'title': ['free', 'giveaway'],
#                           'selftext': ['giveaway']},
#             'pcmasterrace': {'title': ['free', 'giveaway']},
#             'netsec': {'title': ['exploit', 'backdoor', 'hacked', 'vulnerabilities', 'bug']},
#             'linux': {'title': ['exploit', 'backdoor', 'hacked', 'vulnerabilities', 'bug']},
#             'starcitizen': {'author': ['nehkara']}
#             }
# EXCLUDE = {'gamedeals': {'title': ['drm']},
#            'pcmasterrace': {'title': ['drm'],
#                             'selftext': ['drm']},
#            'netsec': {'title': ['challenge', 'exploiting', 'exploited']},
#             'linux': {'title': ['challenge', 'exploiting', 'exploited']},
#            }
#
# SLEEP = 5

SUBREDDITS = []
KEYWORDS = {}
EXCLUDE = {}

SLEEP = 1800

# =============================================================================
# ========================EMAIL INFORMATION====================================
# 
# SENDER_EMAIL = 'blah.bot@gmail.com'
# RECEPIENT_EMAIL = 'blah@gmail.com'
# SUBJECT = 'simple reddit notifier'

SENDER_EMAIL = ''
RECEPIENT_EMAIL = ''
SUBJECT = ''