
USER_AGENT = "Simple reddit notifier 0.1 by /u/deusimpervius"

SUBREDDITS = ['gamedeals', 'pcmasterrace', 'netsec']
KEYWORDS = {'gamedeals': {'title': ['free', 'giveaway'],
                          'selftext': ['giveaway']},
            'pcmasterrace': {'title': ['free', 'giveaway']},
            'netsec': {'title': ['exploit', 'backdoor', 'hacked', 'vulnerabilities', 'bug']},
            'linux': {'title': ['exploit', 'backdoor', 'hacked', 'vulnerabilities', 'bug']}
            }
EXCLUDE = {'gamedeals': {'title': ['drm']},
           'pcmasterrace': {'title': ['drm'],
                            'selftext': ['drm']},
           'netsec': {'title': ['challenge', 'exploiting', 'exploited']},
           'linux': {'title': ['challenge', 'exploiting', 'exploited']},
           }

SLEEP = 5

# =============================================================================
# ========================EMAIL INFORMATION====================================
# 
SENDER_EMAIL = 'abiraf.bot@gmail.com'
RECEPIENT_EMAIL = 'abiraf.bot@gmail.com'
SUBJECT = 'simple reddit notifier'