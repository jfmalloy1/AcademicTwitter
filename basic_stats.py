import pandas as pd
import matplotlib.pyplot as plt
import re
"""  """


def add_dates(df):
    """ Creates a year & date column containing the year a tweet was written

    Should only be used once, at the beginning of the analysis

    Args:
        df (pandas Dataframe): tweet statistics, including writing date
    
    Returns:
        None (dataframe is written to Tweets/tweets.csv)
    """
    years = []
    month = []
    for index, row in df.iterrows():
        years.append(str(row["date"])[:4])
        month.append(str(row["date"])[5:7])

    #Add years and months to dataframe, and re-write tweets.csv to include new dataframe
    df["year"] = years
    df["month"] = month
    df.to_csv("Tweets/tweets.csv")


def year_stats(df, year):
    """ Finds & plots various statistics (e.g., number of tweets) in a year

    Args:
        df (pandas DataFrame): dataframe containing all relevant tweet data (including year)
        year (int): year to be analyzed
    """
    sub_df = df[df["year"] == year]
    print("Size of", year, ":", len(sub_df))

    #plot distribution of tweets across each year
    date_distplot(sub_df, str(year) + "_fulldist")

    #Get queries per year
    with open("Searches/search_terms.txt") as f:
        queries = f.read().splitlines()
        for q in queries:
            query_stats(sub_df, q)


def query_stats(df, query):
    """ Gets various statistics across each query used

    Args:
        df (pandas Dataframe): dataframe of tweets
        query (str): query key to be analyzed
    """
    sub_df = df[df["query"] == query]
    print("Size of", query, ":", len(sub_df))
    date_distplot(sub_df, re.sub("[\"\\'& ]", "", query) + "_fulldist")


def get_hashtags(df):
    """ Get the various hashtags used from a sample of tweets

    Args:
        df (pandas Dataframe): tweet dataframe

    Returns:
        None (hashtags written to Tweets/hashtags.txt)
    """
    hashtags = set()
    for index, row in df.iterrows():
        hs = str(row["hashtags"]).split()
        for h in hs:
            hashtags.add(h)

    print("\n", len(hashtags), "unique hashtags found.")
    #Write hashtags to a file for possible future analyses
    with open("Tweets/hashtags.txt", "w") as f:
        for h in hashtags:
            f.write("%s\n" % h)


""" Get how many geotags were used, and write them to a file """


def geo_tags(df):
    sub_df = df[df["geo"].notna()]
    print(len(sub_df), "geo tags were used")


def date_distplot(df, label):
    """ Plot the month/year of a dataframe

    Args:
        df (pandas dataframe): tweets (with a date column), that should be previously sliced 

    Returns:
        None (saves plots to plots directory)
        
    """
    dates = df["id"].groupby([df["date"].dt.year, df["date"].dt.month]).count()
    dates.plot(kind="bar")
    plt.savefig("plots/" + label + ".png")
    #dates.show()


def main():
    #load tweets csv file
    df = pd.read_csv("Tweets/tweets.csv")
    #remove duplicates
    df = df.drop_duplicates()
    #Set type of date to datetime64
    df["date"] = df["date"].astype("datetime64")

    print("Number of tweets:", len(df) - 1)
    print()

    #Add year and month columns to dataframe - one time function
    #add_dates(df)

    #split database by year
    print("QUERY PER YEAR STATS")
    # for year in [2016, 2017, 2018, 2019, 2020]:
    #     year_stats(df, year)
    # print()

    #Split database by query - read in query and pass it to query_stats function
    print("OVERALL QUERY STATS")
    with open("Searches/search_terms.txt") as f:
        queries = f.read().splitlines()
        for q in queries:
            query_stats(df, q)

    #analyze indidivual hashtags, build a file with all unique hashtags included
    #get_hashtags(df)

    #Analyze geo tags
    geo_tags(df)

    #TEST - test date distribution
    date_distplot(df, "full_test")


if __name__ == "__main__":
    main()
