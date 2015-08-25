

# reddit-notifier


A configurable reddit bot that will notify you through email if a submission matches with keywords you specified .


Installation
-

Clone the repo

   ```
   git clone https://github.com/abirafdirp/reddit-notifier
   ```

Install the requirements

   ```
   pip install -r requirements.txt
   ```

Run it

   ```
   python run.py
   ```

Configuration
-

Below are the configurations that you need to specified in the settings.py

| SETTINGS        | Explanation                                | Example                                                             |
|-----------------|--------------------------------------------|---------------------------------------------------------------------|
| USER_AGENT      | https://github.com/reddit/reddit/wiki/API  | USER_AGENT = "Simple reddit notifier by /u/myaccount" DONT USE THIS |
| SUBREDDITS      | list of subreddits                         | SUBREDDITS = ['gamedeals', 'pcmasterrace']                          |
| KEYWORDS        | SEE BELOW                                  | SEE BELOW                                                           |
| EXCLUDE         | (OPTIONAL) SEE BELOW                       | SEE BELOW                                                           |
| SLEEP           | delay between runs in seconds              | SLEEP = 18000  # 30 minutes                                         |
| SENDER_EMAIL    | a valid gmail account name with @gmail.com |                                                                     |
| RECEPIENT_EMAIL | a valid email address                      |                                                                     |
| SUBJECT         | email subject                              |                                                                     |
Valid Submission Attributes
-
Currently this script only support string attributes, you can find the list of them in the valid_attribute.txt

KEYWORDS
-
Below is an example if you want to match submissions in 'gamedeals' subreddit which has 'free' and 'giveaway' in its title OR 'giveaway' in its selftext. You can also add another keywords for another subreddit in it.
```
KEYWORDS = {'gamedeals': {
                         'title': ['free', 'giveaway'],
                         'selftext': ['giveaway']
                         },
            'netsec': {
                      'title': ['exploit', 'backdoor', 'hacked', 'vulnerabilities', 'bug']
                      }
            }
```

EXCLUDE
-
EXCLUDE is sometimes useful e.g. a free game notifier script that has free in its keywords will catch "DRM free" submission, we don't want that, so we include 'drm' in EXCLUDE. The structure of exclude is same as KEYWORDS. Note that EXCLUDE IS OPTIONAL (currently you need to give it an empty dict).

Below is an example of a free game notifier bot that will exclude any submission if it has 'drm' in its title or its selftext
```
EXCLUDE = {'gamedeals': {
                        'title': ['drm']},
                        'selftext': ['drm']}
		  }
```
Changelog
-
### V 0.1.0 Alpha
* added attribute based keywords

### V 0.0.9
* notify you through email if a submission title match your keywords

to-do
-

* add more valid attributes
* add comment parsing functionality
* more verbose error handling

* ~~match other attribute other than title (configurable)~~
