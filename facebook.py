import os
import facebook
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve your Facebook Page Access Token from the .env file
page_access_token = os.getenv("FACEBOOK_PAGE_ACCESS_TOKEN")

# Initialize the Facebook Graph API object
graph = facebook.GraphAPI(access_token=page_access_token, version="v12.0")

# Set the directory containing your post files
post_directory = "post"

# List all files in the post directory
post_files = os.listdir(post_directory)

# Loop through the post files and post each one
for file_name in post_files:
    file_path = os.path.join(post_directory, file_name)
    caption = "Your caption goes here."

    # Open and upload the file
    with open(file_path, "rb") as image_file:
        graph.put_photo(image=image_file, message=caption)

    print(f"Posted {file_name} to Facebook.")

print("All posts to Facebook completed.")
