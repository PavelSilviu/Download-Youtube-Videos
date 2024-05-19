# YouTube Video Downloader

This simple application allows users to download YouTube videos using the YouTube-DL library. It provides a user-friendly graphical interface built with Tkinter.

## Features

- Downloads YouTube videos by providing the video URL and download path.
- Displays a progress bar indicating the download progress.
- Supports downloading the best video and audio quality available for the given URL.

## Installation

To run the application, you need to have Python installed on your system. Additionally, you'll need to install the following dependencies:

- `tkinter`: GUI library for Python
- `yt-dlp`: YouTube-DL fork with additional features and fixes
- `ffmpeg`: Multimedia framework for handling multimedia data

### Installing Dependencies:

1. **Python and Tkinter:**
   - Install Python from the [official website](https://www.python.org/).
   - Tkinter is included with most Python installations.

2. **yt-dlp:**
   - Install using pip:
     ```bash
     pip install yt-dlp
     ```

3. **ffmpeg:**
   - Download the ffmpeg executable from [ffmpeg official website](https://ffmpeg.org/download.html).
   - Follow the steps provided in [this tutorial](https://phoenixnap.com/kb/ffmpeg-windows) to install ffmpeg on Windows.

## Usage

1. Run the script `youtube_video_downloader.py`.
2. Enter the YouTube URL of the video you want to download.
3. Specify the download path where you want to save the video.
4. Click the "Download" button to start the download process.
5. The progress bar will show the download progress, and a message box will appear upon successful completion or if there's an error.

## Generating Executable

You can generate an executable file using PyInstaller with the following command:

```bash
pyinstaller --onefile --noconsole --icon=icon.ico nume_script.py
