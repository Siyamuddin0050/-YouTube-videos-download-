# import pytube
from pytube import YouTube

# Ask user for the YouTube video URL
url = input("Enter the YouTube video URL: ")

# Create a YouTube object
yt = YouTube(url)

# Get the available video streams for the YouTube video
streams = yt.streams.filter(progressive=True)

# Print the available video quality options
print("Available video quality options:")
for i in range(len(streams)):
    print(f"{i+1}. {streams[i].resolution}")

# Ask user for the video quality option they want to download
option = int(input("Enter the option number for the video quality you want to download: "))

# Get the selected video stream
selected_stream = streams[option-1]

# Get the file size of the selected video stream
file_size = selected_stream.filesize_approx / (1024 * 1024)
print(f"File size: {file_size:.2f} MB")

# Confirm with the user that they want to download the selected video stream
confirm = input("Do you want to download this video? (y/n) ")
if confirm == "y":
    # Download the selected video stream
    print("Downloading...")
    #here path is not given
    selected_stream.download()
    print("Download complete!")
else:
    print("Download cancelled.")
