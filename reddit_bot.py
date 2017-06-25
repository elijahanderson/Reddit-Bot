# praw is a tool that makes interacting with reddit much easier.
#

import praw

# time module is used so the bot won't go crazy

import time
import os

# Login the bot into reddit


def bot_login() :
    print('Logging in...')
    reddit = praw.Reddit(client_id='gZGNheQ3FFswZQ',
                         client_secret='whHLVVFyZJ3VJ5K7joNmCTHuVd4',
                         password='a147258b',
                         user_agent='yeah_bot_test v0.1',
                         username='moldyxorange')
    print('Logged in as ' + str(reddit.user.me()))
    return reddit


def run_bot(reddit, comments_replied_to) :

    # Loop through the top 25 comments in all posts on a certain subreddit
    for comment in reddit.subreddit('test').comments(limit=25) :

        # check if keyword '!showyeahs' is in any of those comments and comment has already been replied to

        if '!showyeahs' in comment.body and comment.id not in comments_replied_to:

            print('String found!!')

            # reply via comment

            comment.reply('String found!! [Yeah!](https://byyeah.com/assets/img/product/outofstock.jpg)')
            print('Replied to ' + comment.id)

            # Add comment ID to replied to list
            comments_replied_to.append(comment.id)

            # Save comment ID to comments_replied_to.txt (the 'a' means i am appending to the file)

            with open('comments_replied_to.txt', 'a') as file:
                file.write(comment.id + '\n')

    # Sleep for ten seconds

    print('Sleeping for 10 seconds...')
    time.sleep(10)

# Save the comments that have been replied to in the past so the bot doesn't reply to same comments the after each time
# it is run
#
# Uses .txt file to store the comments

def get_saved_comments() :

    if not os.path.isfile('comments_replied_to.txt') :
        comments_replied_to = []

    else :
        with open('comments_replied_to.txt', 'r') as file :

            # Read contents of the file
            comments_replied_to = file.read()

            # split() by new line
            comments_replied_to = comments_replied_to.split('\n')

    return comments_replied_to

reddit = bot_login()

# To prevent spam, create list of comments already replied to

comments_replied_to = get_saved_comments()
print(comments_replied_to)
# To automatically reply to comments, a while loop is used

while True :
    run_bot(reddit, comments_replied_to)