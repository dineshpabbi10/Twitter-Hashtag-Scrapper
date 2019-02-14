import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

## Setting Up OAuth .... No need to change Anything..
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

### Creating Pandas DataFrame to store Tweets
t = pd.DataFrame(columns=["Tweets"])

for tweet in tweepy.Cursor(api.search,q="#trump",count=100,lang="en",since="2018-04-03").items():
	if(tweet.text[:2] == "RT"):
		pass
	else:
		t = t.append({"Tweets":tweet.text.replace("\n"," ")},ignore_index=True)
	 
	if len(t)==50:
		break


## To print tweets in console that were stored in the file 
print(t)

## Put the path of the file in the path variable.. Example path = r"G:\sss.csv"
path = r""
t.to_csv(path)
