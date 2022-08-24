import GetOldTweets3 as got
import time
import pandas as pd


def get_date_pairs():
    """ Set up dates - in 3 month intervals - for fine-grained analyses 
    
    Args:
        None

    Returns:
        pairs (list): date pairs from Jan 1 2016 to mid-June 2020 in 3 month interval 
    """

    pairs = []
    #3-month intervals for all years from 2016-2019
    for year in ["2016", "2017", "2018", "2019"]:
        pairs.append([year + "-01-01", year + "-03-31"])
        pairs.append([year + "-04-01", year + "-06-30"])
        pairs.append([year + "-07-01", year + "-09-30"])
        pairs.append([year + "-10-01", year + "-12-31"])
    #Add 2020
    pairs.append(["2020-01-01", "2020-03-31"])
    pairs.append(["2020-04-01", "2020-06-17"])

    return pairs


def get_search_terms():
    """ Set up search terms 
 
    Args: 
        None

    Returns:
        list: all search terms within Searches/search_terms.txt

    """
    with open("Searches/search_terms.txt") as f:
        lines = f.read().splitlines()
    return lines


def main():
    #Criteria for tweets
    max_tweets = 10000

    df = pd.DataFrame(columns=[
        "query", "id", "permalink", "username", "to", "text", "date",
        "retweets", "favorites", "mentions", "hashtags", "geo"
    ])

    date_pairs = get_date_pairs()
    search_terms = get_search_terms()

    #Actual tweet scraping
    #Loop through interval pairs
    for dates in date_pairs:
        #Loop through each search term
        for term in search_terms:
            #Set up criteria based on date and search term
            tweetCriteria = got.manager.TweetCriteria().setQuerySearch(
                term).setSince(dates[0]).setUntil(
                    dates[1]).setMaxTweets(max_tweets)

            #Actually get the tweets - timed along the way
            start = time.time()
            tweets = got.manager.TweetManager.getTweets(tweetCriteria)
            end = time.time()

            #TODO: clean up tweets (grammar, capitalization, "my hero academia", etc...)

            #create a list of each tweet to add to dataframe (GetOldTweets3 doesn't work with a one-line append)
            for t in tweets:
                l = [term]
                l.append(t.id)
                l.append(t.permalink)
                l.append(t.username)
                l.append(t.to)
                l.append(t.text)
                l.append(t.date)
                l.append(t.retweets)
                l.append(t.favorites)
                l.append(t.mentions)
                l.append(t.hashtags)
                l.append(t.geo)
                #print(t.id)
                #check if df is empty - if so, index = 0. Otherwise, add to max index + 1
                if len(df) == 0:
                    df.loc[0] = l
                else:
                    df.loc[df.index.max() + 1] = l
            print("Time for", max_tweets, term, dates, "tweets:", end - start)

    df.to_csv("tweets.csv")


if __name__ == "__main__":
    main()
