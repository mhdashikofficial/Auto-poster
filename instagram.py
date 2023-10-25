import os
import instabot
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve your Instagram username and password from .env file
instagram_username = os.getenv("INSTAGRAM_USERNAME")
instagram_password = os.getenv("INSTAGRAM_PASSWORD")

# Initialize the Instagram bot
bot = instabot.Bot()

# Login to Instagram
bot.login(username=instagram_username, password=instagram_password)

# Set the directory containing your post files
post_directory = "post"

# List all files in the post directory
post_files = os.listdir(post_directory)

# Loop through the post files and post each one
for file_name in post_files:
    file_path = os.path.join(post_directory, file_name)
    caption = ""
    
    if file_name.endswith((".jpg", ".jpeg", ".png", ".gif")):
        # If the file is an image, use it as an attachment
        bot.upload_photo(file_path, caption=caption)
    elif file_name.endswith((".mp4")):
        # If the file is a video, use it as an attachment
        bot.upload_video(file_path, caption=caption)

# Logout from Instagram
bot.logout()
