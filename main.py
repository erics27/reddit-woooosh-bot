import praw
import re

# goto reddit.com/prefs/apps

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="",
    username="",
    password=""
)

subreddit = reddit.subreddit("wooooshbottesting")

for submission in subreddit.hot():

    submission.comments.replace_more(limit=None)

    for comment in submission.comments.list():

        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if "r/woooosh" in comment_lower:
                print(comment_lower)
            else:
                spelled_wrong = re.search("r\/w+h*o+s+h+", comment_lower)
                if spelled_wrong:
                    print(comment_lower)
                    comment.reply("It's r/woooosh\n *** \n *I'm a bot*")
