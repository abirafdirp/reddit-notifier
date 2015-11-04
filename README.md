

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

License
-
License Copyright (c) 2015, Abirafdi Raditya Putra All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
