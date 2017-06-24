# praw is a tool that makes interacting with reddit much easier.
#

import praw

# Login the bot into reddit


def bot_login() :
    print('Logging in...')
    reddit = praw.Reddit(client_id='kQ-LllZafD8X5Q',
                         client_secret='wB-SNo-_ImXjPIVCKaFjbobP_Zg',
                         password='elephantsanddonkeysgrowbigears',
                         user_agent='yeah_bot_test v0.1',
                         username='yeah_bot_test')
    print('Logged in as ' + str(reddit.user.me()))
    return reddit


def run_bot(reddit) :

    # Loop through the top 25 comments in all posts on a certain subreddit
    for comment in reddit.subreddit('test').comments(limit=25) :

        #check if keyword '!showyeahs' is in any of those comments

        if '!showyeahs' in comment.body :
            print('String found!!')         #Placeholder for code that will be implemented at later time


reddit = bot_login()
run_bot(reddit)