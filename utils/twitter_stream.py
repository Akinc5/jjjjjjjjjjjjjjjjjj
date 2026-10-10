import tweepy
import json

# Set these from your Twitter Developer Portal
TWITTER_BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAANOB2wEAAAAAvZDgTaCLLLXq1VoYubScGOlIBjs%3Dh0BlOB2IOrWp3C1tyWZfecTONf4M06Mhk61i4dZNYPbaMCwIig"

def get_bangalore_tweets(query="Banglore flood OR traffic OR rain", max_results=10):
    client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)
    
    # Remove unsupported 'place:' operator
    tweets = client.search_recent_tweets(
        query=query + " lang:en", 
        max_results=max_results,
        tweet_fields=["created_at"]
    )

    results = []
    if tweets.data:
        for tweet in tweets.data:
            results.append({
                "source": "twitter",
                "text": tweet.text,
                "timestamp": tweet.created_at.isoformat()
            })
    return results
