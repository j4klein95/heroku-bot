import tweepy
import time
import json
import random
import requests as req
import datetime
import os
#import config

#config = "./config.py"


# Twitter API Keys
consumer_key = os.environ.get('consumer_key')
#config.consumer_key
consumer_secret = os.environ.get('consumer_secret')
#config.consumer_secret
access_token = os.environ.get('access_token')
#config.access_token
access_token_secret = os.environ.get('access_token_secret')
#config.access_token_secret

# Weather API
api_key = os.environ.get('api_key')
#config.api_key


# Create a function that gets the weather in London and Tweets it
def WeatherTweet():

    # Construct a Query URL
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "London"
    units = "imperial"
    query_url = url + "appid=" + api_key + "&q=" + city + "&units=" + units

    # Perform the API 
    weather_response = req.get(query_url)
    weather_json = weather_response.json()
    print(weather_json)

    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet the weather
    api.update_status(
        "London Weather as of %s: %s F" %
        (datetime.datetime.now().strftime("%I:%M %p"),
         weather_json["main"]["temp"]))

    # Print success message
    print("Tweeted successfully, sir!")


# Set timer to run every 1 hour
while(True):
    WeatherTweet()
    time.sleep(3600)
