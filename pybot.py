import praw
import time

r = praw.Reddit(user_agent = "First Bot by /u/userID")
print "Logging In..."
r.login('userID', "password")

words_to_match = ["christmas", "merry"]
cache = []

def run_bot():
    print "Grabbing Subreddit..."
    subreddit = r.get_subreddit("test")
    comments = subreddit.get_comments(limit = 25)
    print "Grabbing Comments..."
    for comment in comments:
        isMatch = False
        comment_text = comment.body.lower()
        #isMatch = any(str in comment_text for string in words_to_match)
        for i in comment_text.split():
            if i in words_to_match:
                isMatch = True
        if comment.id not in cache and isMatch:
            print "Match found! Comment ID: " + comment.id
            comment.reply("And Same to you!")
            cache.append(comment.id)

    print "Comments loop finished, time to sleep."

while True:
    run_bot()
    time.sleep(10)
