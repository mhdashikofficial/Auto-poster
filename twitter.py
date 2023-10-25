import os
import tweepy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve your Twitter API keys and access tokens from the .env file
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Initialize the Twitter API object
api = tweepy.API(auth)

# Set the directory containing your post files
post_directory = "post"

# List all files in the post directory
post_files = os.listdir(post_directory)

# Loop through the post files and post each one
for file_name in post_files:
    file_path = os.path.join(post_directory, file_name)
    caption = "Your caption goes here."

    if file_name.endswith((".jpg", ".jpeg", ".png", ".gif")):
        # If the file is an image, use it as an attachment
        api.update_with_media(filename=file_path, status=caption)
    elif file_name.endswith((".mp4")):
        # If the file is a video, use it as an attachment
        api.update_with_media(filename=file_path, status=caption, media_category="tweet_video")

    print(f"Posted {file_name} to Twitter.")

print("All posts to Twitter completed.")
