import tweepy
from GoogleNews import GoogleNews
import json

# Twitter API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Function to get tweets
def get_tweets(username, count):
    tweets = api.user_timeline(screen_name=username, count=count, tweet_mode="extended")
    tweet_list = []
    for tweet in tweets:
        tweet_list.append({"created_at": tweet.created_at, "text": tweet.full_text})
    return tweet_list

# Function to get news articles
def get_news(query, count):
    googlenews = GoogleNews()
    googlenews.search(query)
    news_list = googlenews.get_texts()[:count]
    return news_list

# Main function
def main():
    # Get tweets
    username = "elonmusk"
    tweet_count = 5
    tweets = get_tweets(username, tweet_count)
    print(f"Latest {tweet_count} tweets from {username}:")
    for tweet in tweets:
        print(f"{tweet['created_at']}: {tweet['text']}")

    # Get news articles
    query = "technology"
    news_count = 5
    news_articles = get_news(query, news_count)
    print(f"\nTop {news_count} news articles for '{query}':")
    for article in news_articles:
        print(article)

if __name__ == "__main__":
    main()
