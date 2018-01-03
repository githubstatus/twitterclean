#!/usr/bin/env python
# encoding: utf-8

import time
import sys
import os
from dotenv import load_dotenv, find_dotenv
import twitter

def main(argv=None):
    load_dotenv(find_dotenv())

    api = twitter.Api(
    consumer_key=os.environ.get("consumer_key"),
    consumer_secret = os.environ.get("consumer_secret"),
    access_token_key = os.environ.get("access_token_key"),
    access_token_secret = os.environ.get("access_token_secret"))

    REMOVE_TWEETS = True
    REMOVE_RETWEETS = True
    REMOVE_FAVORITES = True
    DRY_RUN = True

    while REMOVE_FAVORITES:
        print("\n FAVORITES:\n")
        favorites = api.GetFavorites(count=200)
        if len(favorites) == 0:
            print("\nNo remaining favorites found...")
            break
        for favorite in favorites:
            try:
                print("\nFavorite id: ", favorite.id)
                if (DRY_RUN == False):
                    # status = api.DestroyFavorite(status_id=favorite.id)
                    print(status)
                else:
                    print("Dry run")
                time.sleep(1)
            except Exception as e:
                pass
                time.sleep(1)

    while REMOVE_RETWEETS:
        print("\n RETWEETS:\n")
        tweets = api.GetUserTimeline(count=200, include_rts=True)
        if len(tweets) == 0:
            print("\nNo remaining tweets found...")
            break
        for tweet in tweets:
            print("Found tweet, scanning...")
            try:
                if (tweet.retweeted == True):
                    print("\n Retweet id: ", tweet.id)
                    if (DRY_RUN == False):
                        # status = api.DestroyStatus(tweet.id)
                        print(status)
                    else:
                        print("Dry run")
                time.sleep(2)
            except Exception as e:
                pass
                time.sleep(1)

    while REMOVE_TWEETS:
        print("\n TWEETS:\n")
        tweets = api.GetUserTimeline(count=200, include_rts=False)
        if len(tweets) == 0:
            print("\nNo remaining tweets found...")
            break
        for tweet in tweets:
            print("Found tweet, deleting...")
            try:
                if (DRY_RUN == False):
                    print("\n Tweet id: ", tweet.id)
                    # status = api.DestroyStatus(tweet.id)
                    print(status)
                else:
                    print("Dry run")
                time.sleep(2)
            except Exception as e:
                pass
                time.sleep(1)

if __name__ == "__main__":
    sys.exit(main())
    