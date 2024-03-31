#!/usr/bin/env python3

"""
A python3 script to find music files form youtube then download them as mp4 files.

"""

import argparse
import subprocess

def download_youtube_video(url):
    """
    Downloads a YouTube video as an mp3 file.

    Args:
    url (str): The URL of the YouTube video to download.

    Returns:
    None
    """
    # Use youtube-dl to download the video as an mp3 file
    #subprocess.call(['youtube-dl', '-x', '--audio-format', 'mp3', url])
    subprocess.call(['yt-dlp', '-x', '--audio-format', 'mp3', "-P", "~/Music/", url])
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download a YouTube video as an mp3 file.')
    parser.add_argument('-u', '--url', type=str, help='The URL of the YouTube video to download.')
    args = parser.parse_args()

    download_youtube_video(args.url)