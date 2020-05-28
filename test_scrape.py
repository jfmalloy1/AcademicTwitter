import GetOldTweets3 as got
import re
import time

def main():
    #Criteria for tweets
    max_tweets = [10, 100, 1000, 10000, 100000, 1000000]

    #tweetCriteria = got.manager.TweetCriteria().setQuerySearch("'leaving' & 'academia'").setSince("2020-05-01").setMaxTweets(max_tweets)

    #Actual tweet scraping
    for size in max_tweets:
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch("academia").setSince("2016-05-01").setMaxTweets(size)

        start = time.time()
        tweets = got.manager.TweetManager.getTweets(tweetCriteria)
        end = time.time()

        #TODO: clean up tweets (grammar, capitalization, "my hero academia", etc...)

        #How many tweets didn't include "my hero"
        print("Size:", len(tweets))
        print("Time for", size, "tweets:", end-start)

if __name__ == "__main__":
    main()
