""" Goal: find the negative to positive word ratio for each quarter within dataset"""
import pandas as pd


def get_sentiment(df, year, start_month, end_month, neg, pos):
    #Isolate date-specific tweets
    sub_df = df[df["year"] == year]
    sub_df = sub_df[sub_df["month"] <= end_month]
    sub_df = sub_df[sub_df["month"] >= start_month]

    #Count number of positive and negative words
    neg_count = 0
    pos_count = 0
    for index, row in sub_df.iterrows():
        txt = str(row["text"]).split(' ')
        for word in txt:
            if word in neg:
                neg_count += 1
            if word in pos:
                pos_count += 1

    print("Negative:Positive ratio for months", start_month, "-", end_month,
          "in", year, "is:", neg_count, "to", pos_count,
          "(" + str(round(neg_count / pos_count, 3)) + ")")


def main():
    #Read in negative and positive words
    neg_file = open("PosNeg_Words/negative_words.txt", "r")
    neg = neg_file.read().split("\n")
    neg_file.close()

    pos_file = open("PosNeg_Words/positive_words.txt", "r")
    pos = pos_file.read().split("\n")
    pos_file.close()

    #TEST: find ratio of negative and positive words within 1st quarter of data
    df = pd.read_csv("Tweets/tweets.csv")
    for year in [2016, 2017, 2018, 2019, 2020]:
        get_sentiment(df, year, 1, 3, neg, pos)
        get_sentiment(df, year, 4, 6, neg, pos)
        if year != 2020:
            get_sentiment(df, year, 7, 9, neg, pos)
            get_sentiment(df, year, 10, 12, neg, pos)


if __name__ == "__main__":
    main()
