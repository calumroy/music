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
    parser.add_argument('url', nargs='?', help='The URL of the YouTube video to download.')
    parser.add_argument('-u', '--url-flag', type=str, help='The URL of the YouTube video to download (alternative flag).')
    args = parser.parse_args()

    # Use positional argument if provided, otherwise use flag
    url = args.url or args.url_flag
    
    if not url:
        parser.error('Please provide a YouTube URL either as a positional argument or using -u flag')
    
    download_youtube_video(url)