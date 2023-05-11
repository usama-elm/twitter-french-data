import tweepy
import pandas as pd
import csv
import re 
import string
import requests
import preprocessor as p
from keys import *

nombre=100

client = tweepy.Client( bearer_token=bearer_token, 
                        consumer_key=consumer_key, 
                        consumer_secret=consumer_secret,  
                        return_type = requests.Response,
                        wait_on_rate_limit=True)

query = 'vaccins'
tweets = client.search_recent_tweets(query=query, 
                                    tweet_fields=['author_id', 'created_at'],
                                     max_results=nombre)


tweets_dict = tweets.json() 

tweets_data = tweets_dict['data'] 

df = pd.json_normalize(tweets_data)
df.to_csv("vaccinsOff.csv")