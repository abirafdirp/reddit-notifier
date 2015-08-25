
USER_AGENT = "Simple reddit notifier 0.1 by /u/deusimpervius"

SUBREDDITS = ['gamedeals', 'starcitizen']
KEYWORDS = {'gamedeals': [{'title': ['free', 'giveaway']},
                          {'selftext': ['giveaway']}],
            'starcitizen': [{'title': ['chairman']}]
            }
EXCLUDE = {'gamedeals': [{'title': ['drm']}],
           'starcitizen': [{'url': ['imperialnews']}]
           }

SLEEP = 5

# =============================================================================
# ========================EMAIL INFORMATION====================================
# 
SENDER_EMAIL = 'abiraf.bot@gmail.com'
RECEPIENT_EMAIL = 'abiraf.bot@gmail.com'
SUBJECT = 'simple reddit notifier'