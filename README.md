# -YouTube-videos-download-
this code helps you to download YouTube videos in your laptop or PC using python 
Install Pytube: Open your command prompt or terminal and type pip install pytube to install Pytube library.

Import the Pytube library: To use the Pytube library in your Python script, you need to import it at the beginning of your script using the following code:

from pytube import YouTube


Create a YouTube object: To download a video, you need to create a YouTube object by passing the URL of the video to the constructor. For example:

video = YouTube('https://www.youtube.com/watch?v=video_id')

Replace the video_id with the actual video ID that you want to download.

Print available video resolutions: To see the available video resolutions, use the following code:

print(video.streams.all())

This will print a list of all the available streams, along with their resolution, file type, and other information.

Download the video: To download the video, use the following code:

video.streams.get_highest_resolution().download()

This will download the video in the highest available resolution.

That's it! With these steps, you can download a YouTube video in Python using the Pytube library.

also 

You can use the Pytube library to download YouTube videos in Python. Here's a sample code:

from pytube import YouTube

# Paste the URL of the YouTube video you want to download
url = "https://www.youtube.com/watch?v=video_id"

# Create a YouTube object
video = YouTube(url)

# Print the available video resolutions
print(video.streams.all())

# Download the video in the highest resolution
video.streams.get_highest_resolution().download()
