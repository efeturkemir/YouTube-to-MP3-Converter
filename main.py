from pytube import YouTube
from moviepy.editor import *
import os

def convert_to_mp3(video_url):
    try:
        # Fetch YouTube video
        yt = YouTube(video_url)

        # Download the highest quality video
        video = yt.streams.get_highest_resolution()
        video.download()

        # Set the path to the downloaded video file
        video_path = video.default_filename

        print(f"Downloaded video path: {video_path}")

        # Extract audio and save as MP3
        mp4_file = video_path
        mp3_file = video_path[:-4] + '.mp3'
        video = VideoFileClip(mp4_file)
        video.audio.write_audiofile(mp3_file)
        
        video.close()
        os.remove(mp4_file)

        print(f"MP3 file '{mp3_file}' created successfully!")

    except Exception as e:
        print(f"Error: {str(e)}")

# Example usage
video_url = input("Enter the YouTube video URL: ")
convert_to_mp3(video_url)