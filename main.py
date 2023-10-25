import tkinter as tk
from tkinter import filedialog
import subprocess
import os

def add_caption_hashtags():
    caption = caption_entry.get()
    hashtags = hashtags_entry.get()
    
    # Create a new directory named "post" if it doesn't exist
    if not os.path.exists("post"):
        os.mkdir("post")
    
    with open(os.path.join("post", "post.txt"), "a") as file:
        file.write(f"Caption: {caption}\nHashtags: {hashtags}\n")

def attach_files():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp *.ppm *.pgm")])
    
    # Create a new directory named "post" if it doesn't exist
    if not os.path.exists("post"):
        os.mkdir("post")
    
    with open(os.path.join("post", "post.txt"), "a") as file:
        file.write(f"Attachment: {file_path}\n")

def post_content():
    subprocess.call(["python", "instagram.py"])
    subprocess.call(["python", "facebook.py"])
    subprocess.call(["python", "twitter.py"])
    subprocess.call(["python", "telegram.py"])
    status_label.config(text="Posting complete!")

# Create the main window
root = tk.Tk()
root.title("Auto Poster Tool")

# Create and configure widgets
caption_label = tk.Label(root, text="Caption:")
caption_label.pack()
caption_entry = tk.Entry(root)
caption_entry.pack()

hashtags_label = tk.Label(root, text="Hashtags:")
hashtags_label.pack()
hashtags_entry = tk.Entry(root)
hashtags_entry.pack()

add_caption_hashtags_button = tk.Button(root, text="Add Caption and Hashtags", command=add_caption_hashtags)
add_caption_hashtags_button.pack()

attach_files_button = tk.Button(root, text="Attach Image", command=attach_files)
attach_files_button.pack()

post_button = tk.Button(root, text="Post", command=post_content)
post_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

# Start the GUI event loop
root.mainloop()
