import tweepy
from textblob import TextBlob
consumer_key="JVV81nooZixtO4wO5FF2cPggH"
consumer_secret="u4uMWu4s1I2SfUpSOmMx8BJYBzoACB4IvMYPpPxLjRAZXyvLD6"

access_token="143747055-QHLNrPudaT2iIX5Q0zJI4RlnykijJqY4T48kleXt"
access_token_secret="Zzcz8jfMwDWDgOyb1IkXnPZCTi2N8RI9oMFcuJVqOHKVr"

auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

public_tweets=api.search('Modi')
print(len(public_tweets))
for tweet in public_tweets:
	print(tweet.text)
	analysis=TextBlob(tweet.text)
	print(analysis.sentiment)