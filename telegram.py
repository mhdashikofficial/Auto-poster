from pyrogram import Client, InputFile
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve your Telegram API credentials and chat ID from the .env file
api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

# Initialize the Pyrogram client
with Client("my_account", api_id=api_id, api_hash=api_hash) as app:
    # Set the directory containing your post files
    post_directory = "post"

    # List all files in the post directory
    post_files = os.listdir(post_directory)

    # Loop through the post files and send each one
    for file_name in post_files:
        file_path = os.path.join(post_directory, file_name)
        caption = "Your caption goes here."

        if file_name.endswith((".jpg", ".jpeg", ".png", ".gif")):
            # If the file is an image, send it as a photo
            app.send_photo(chat_id, photo=InputFile(file_path), caption=caption)
        elif file_name.endswith((".mp4")):
            # If the file is a video, send it as a video
            app.send_video(chat_id, video=InputFile(file_path), caption=caption)

        print(f"Sent {file_name} to Telegram.")

    print("All posts to Telegram completed.")
