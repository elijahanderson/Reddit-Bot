# praw is a tool that makes interacting with reddit much easier.
#

import praw

# time module is used so the bot won't go crazy

import time

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


def run_bot(reddit, comments_replied_to) :

    # Loop through the top 25 comments in all posts on a certain subreddit
    for comment in reddit.subreddit('test').comments(limit=25) :

        #check if keyword '!showyeahs' is in any of those comments and comment has already been replied to

        if '!showyeahs' in comment.body and comment.id not in comments_replied_to:
            print('String found!!')         #Placeholder for code that will be implemented at later time

            #reply via comment

            comment.reply('String found!! [Yeah!](https://byyeah.com/assets/img/product/outofstock.jpg)')
            print('Replied to ' + comment.id)

            # Add comment ID to replied to list
            comments_replied_to.append(comment.id)

            # Sleep for ten seconds

            print('Sleeping for 10 seconds...')
            time.sleep(10)

    # Sleep for ten seconds

    print('Sleeping for 10 seconds...')
    time.sleep(10)

reddit = bot_login()

# To prevent spam, create list of comments already replied to

comments_replied_to = []

# To automatically reply to comments, a while loop is used

while True :
    run_bot(reddit, comments_replied_to)