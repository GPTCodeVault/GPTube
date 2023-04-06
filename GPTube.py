import os
import re
from pytube import YouTube
from moviepy.editor import *

def download_video(url, save_path, file_format):
    try:
        yt = YouTube(url)
        print("Title:", yt.title)
        print("Author:", yt.author)
        print("Duration:", yt.length, "seconds")

        # Remove special characters and replace them with underscores
        cleaned_title = re.sub('[^0-9a-zA-Z]+', '_', yt.title)

        if file_format == "mp4":
            stream = yt.streams.get_highest_resolution()
            print("Downloading video...")
            stream.download(save_path, filename=cleaned_title + ".mp4")
        elif file_format == "mp3":
            stream = yt.streams.get_audio_only()
            print("Downloading audio...")
            audio_file = stream.download(save_path, filename_prefix="temp_")
            print("Converting to mp3...")

            audio = AudioFileClip(audio_file)
            output_audio = os.path.join(save_path, cleaned_title + ".mp3")
            audio.write_audiofile(output_audio, codec='mp3', bitrate="128k")

            os.remove(audio_file)

    except Exception as e:
        print("Failed to download the video. Please check the URL and try again.")
        print("Error:", e)

if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    save_path = input("Enter the path where you want to save the file (default is current directory): ")
    file_format = input("Choose the file format (mp3 or mp4): ")

    download_video(url, save_path, file_format)
