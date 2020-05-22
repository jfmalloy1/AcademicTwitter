import GetOldTweets3 as got
import re

def main():
    #Criteria for tweets
    max_tweets = 100
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('leaving academia').setSince("2020-05-01").setMaxTweets(max_tweets)

    #Actual tweet scraping
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    count = 0
    for tweet in tweets:
        #Stupid removal of TV show called "my hero"
        if "my hero" not in tweet.text:
            count += 1
            print(tweet.text)

    #How many tweets didn't include "my hero"
    print("Actual academic tweets:", count)

if __name__ == "__main__":
    main()
