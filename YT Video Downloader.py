import tkinter as tk
from tkinter import ttk, messagebox
from yt_dlp import YoutubeDL
import os
import threading

def download_video():
    url = url_entry.get()
    path = path_entry.get()
    download_type = download_type_var.get()
    if url and path:
        if not os.path.exists(path):
            messagebox.showwarning("Path Error", "The specified path does not exist.")
            return
        threading.Thread(target=download_thread, args=(url, path, download_type)).start()
    else:
        messagebox.showwarning("Input Error", "Please enter a valid YouTube URL and path.")

def download_thread(url, path, download_type):
    try:
        if download_type == 'Video':
            ydl_opts = {
                'progress_hooks': [progress_function],
                'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
                'format': 'bestvideo[height<=?1080]+bestaudio/best'
            }
        else:
            ydl_opts = {
                'progress_hooks': [progress_function],
                'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", f"{download_type} downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download {download_type}: {e}")

def progress_function(data):
    if data['status'] == 'downloading':
        filename = os.path.basename(data['filename'])
        video_extensions = ['.mp4', '.webm', '.mkv', '.avi']
        if any(ext in filename for ext in video_extensions):
            if data.get('total_bytes') is not None:
                total_size = data['total_bytes']
                downloaded = data['downloaded_bytes']
                percentage = (downloaded / total_size) * 100
                root.after(100, update_progress, percentage)
    elif data['status'] == 'finished':
        progress_bar['value'] = 0

def update_progress(percentage):
    progress_bar['value'] = percentage

# Set up the GUI
root = tk.Tk()
root.title("YouTube Video Downloader")

tk.Label(root, text="Enter YouTube URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Set default path to the Downloads folder on Windows
default_download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
path_entry = tk.Entry(root, width=50)
path_entry.insert(0, default_download_path)  # Insert default path
path_entry.pack(pady=5)

tk.Label(root, text="Select Download Type:").pack(pady=5)
download_type_var = tk.StringVar(value='Video')
download_type_menu = ttk.OptionMenu(root, download_type_var, 'Video', 'Video', 'Audio')
download_type_menu.pack(pady=5)

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=10)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=10)

root.mainloop()
