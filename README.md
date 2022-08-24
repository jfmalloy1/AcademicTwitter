# AcademicTwitter
Exploring trends in academic twitter

## Eventual Goal

Perform full sentiment analysis over tweet data.

Some helpful articles are listed below:
- https://realpython.com/python-nltk-sentiment-analysis/ (uses NLTK)
- https://www.datacamp.com/tutorial/simplifying-sentiment-analysis-python (Naive Bayes)
- https://techvidvan.com/tutorials/python-sentiment-analysis/ (uses TensorFlow)
- https://www.analyticsvidhya.com/blog/2021/06/rule-based-sentiment-analysis-in-python/ (uses NLTK's VADER)

## Scripts description & goals

```
test_scrape.py
```

Scrapes tweet data, filtered through search terms in `search_terms.txt`

Date range is hard-coded in `get_search_terms()` method - change this for additional dates. Currently set to 3-month time periods from 2016-2020 (up through mid-June)

Necessary packages: `pandas`, `time`, `GetOldTweets3` [package here](https://pypi.org/project/GetOldTweets3/)

```
basic_stats.py
```

Generates basic statistics & plots about tweets obtained through `test_scrape.py`

Current statistics: total number of tweets, tweets obtained from each query in `search_terms.txt`, hashtags & geotages used within total tweet set

``` 
neg_pos_ratio.py
```

Finds the ratio of negative to positive words within tweet dataset

Uses predefined sets of negative and positive words (in `PosNeg_Words` directory) to generate ratios
