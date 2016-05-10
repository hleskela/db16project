import praw
import re

def print_thread(obj):
    print(str(obj))

def print_comments(post):
    print("in print_comments")
    for comment in post:
        print("in print_comments for loop")
        print(comment.body)

user_agent = "DB16app by DB16scraper, woo us!"
subreddits = ["AskReddit","funny","todayilearned","pics","science","worldnews","IAmA","announcements","videos","gaming","blog","movies","Music","aww","news","gifs","explainlikeimfive","askscience","EarthPorn","books","television","LifeProTips","mildlyinteresting","DIY","sports","Showerthoughts","space","Fitness","tifu","Jokes","InternetIsBeautiful","food","photoshopbattles","gadgets","history","nottheonion","dataisbeautiful","Futurology","GetMotivated","Documentaries","personalfinance","listentothis","philosophy","UpliftingNews","OldSchoolCool","The_Donald","TrollXChromosomes","TwoXChromosomes","SandersForPresident", "BlackPeopleTwitter"]
r = praw.Reddit(user_agent=user_agent)
top_posts_per_subreddit = [ r.get_subreddit(x).get_top_from_year(limit=100) for x in subreddits ]

POST_ID = 0 

for subreddit in top_posts_per_subreddit:
    #threads = [print_thread(thread) for thread in subreddit]
    for thread in subreddit:
        i = 0
        real_comments = [comment for comment in thread.comments if isinstance(comment, praw.objects.Comment)]
        real_comments.sort(key=lambda comment: comment.score, reverse=True)
        
        for comment in real_comments:
            user = comment.author
            print(str(POST_ID) + ",\"" + str(thread.title).replace("\"","\"\"") + "\"," + str(user) + ",\""+ str(comment.body).replace("\"","\"\"")+ "\"")
            POST_ID = POST_ID+1
            i = i+1
   

