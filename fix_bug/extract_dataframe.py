import json
import pandas as pd
from textblob import TextBlob

def read_json(json_file: str)->list:
    """
    json file reader to open and read json files into a list
    Args:
    -----
    json_file: str - path of a json file
    
    Returns
    -------
    length of the json file and a list of json
    """
    
    tweets_data = []
    for tweets in open(json_file,'r'):
        tweets_data.append(json.loads(tweets))
    
    
    return len(tweets_data), tweets_data

class TweetDfExtractor:
    """
    this function will parse tweets json into a pandas dataframe
    
    Return
    ------
    dataframe
    """
    def __init__(self, tweets_list):
        
        self.tweets_list = tweets_list

    # an example function
    def find_statuses_count(self)->list:
        statuses_count =[]
        statuses_count = []
        for tweet in self.tweets_list:
            statuses_count.append(tweet['user']['statuses_count'])
        return statuses_count
        
    def find_full_text(self)->list:
        text = text = []
        for tweet in self.tweets_list:
            if 'retweeted_status' in tweet.keys() and 'text' in tweet['retweeted_status'].keys():
                text.append(tweet['retweeted_status']['text'])
            else:
                text.append('Empty')
        return text
    def find_sentiments(self, text: list) -> list:
        polarity = []
        subjectivity = []
        for tweet in text:
            blob = TextBlob(tweet)
            sentiment = blob.sentiment
            polarity.append(sentiment.polarity)
            subjectivity.append(sentiment.subjectivity)
        return polarity, subjectivity
    def find_created_time(self) -> list:
        created_at = []
        for time in self.tweets_list:
            created_at.append(time['created_at'])
        return created_at
    def find_source(self) -> list:
        source = []
        for x in self.tweets_list:
            source.append(x['source'])
        return source