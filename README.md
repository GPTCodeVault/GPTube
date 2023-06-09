GPTube
========================

This is a simple Python script that allows you to download YouTube videos as MP4 or MP3 files. It uses `pytube` and `moviepy` libraries to handle video download and conversion. Due to the limitations of PyTube, the downloaded video quality is subpar.

Features
--------

*   Download YouTube videos in MP4 format
*   Download YouTube videos as MP3 audio files

Requirements
------------

*   Python 3.x
*   pytube
*   moviepy

Installation
------------

1.  Clone the repository:

    git clone https://github.com/GPTCodeVault/GPTube.git

3.  Change the working directory:

    cd GPTube

5.  Install the required dependencies:

    pip install -r requirements.txt

Usage
-----

1.  Run the script:

    py GPTube.py

3.  Follow the prompts to enter the YouTube video URL, save path, and desired file format (MP4 or MP3).

Examples
--------

Here's an example of how to use the script:

    
    Enter the YouTube video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
    Enter the path where you want to save the file (default is current directory): /path/to/save/directory
    Choose the file format (mp3 or mp4): mp4
    

The script will download the video, convert it to the chosen format, and save it to the specified directory.

A Message from ChatGPT
----------------------

Hello! I am ChatGPT, an AI language model developed by OpenAI. I hope you find this YouTube Video Downloader script useful. If you have any questions, feedback, or suggestions, feel free to create an issue on the GitHub repository or contribute to the project. Happy downloading!
