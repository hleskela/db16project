import praw

def print_thread(obj):
    print(str(obj))

def print_comments(post):
    print("in print_comments")
    for comment in post:
        print("in print_comments for loop")
        print(comment.body)

print("Initializing crawler...")
user_agent = "DB16app by DB16scraper, woo us!"
subreddits = ["todayilearned", "science", "askscience","space","AskHistorians","YouShouldKnow","explainlikeimfive"]
r = praw.Reddit(user_agent=user_agent)
print("Fetching subreddit posts...")
top_posts_per_subreddit = [ r.get_subreddit(x).get_hot(limit=5) for x in subreddits ]

for subreddit in top_posts_per_subreddit:
    print("Post:")
    #threads = [print_thread(thread) for thread in subreddit]
    for thread in subreddit:
        i = 0
        print(i)
        print(thread)
        for comment in thread.comments:
            if not isinstance(comment, praw.objects.MoreComments):
                print(comment.body)
            print(i)
            i = i+1
    print("Comment:")
   

