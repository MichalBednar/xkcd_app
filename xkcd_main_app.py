
import os
from dotenv import load_dotenv
import tweepy
from xkcd_app import GetXkcdData

load_dotenv()

auth = tweepy.OAuthHandler(os.getenv("consumer_key"),
                           os.getenv("consumer_secret"))

auth.set_access_token(os.getenv("access_token"),
                      os.getenv("access_token_secret"))

api = tweepy.API(auth)

a = GetXkcdData()

# Upload actual picture with text on Twitter
api.update_with_media(a.download_xkcd_comic(), a.post_title())