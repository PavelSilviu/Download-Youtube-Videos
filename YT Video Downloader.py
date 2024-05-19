import tkinter as tk
from tkinter import ttk, messagebox
from yt_dlp import YoutubeDL
import os
import threading

def download_video():
    url = url_entry.get()
    path = path_entry.get()
    if url and path:
        if not os.path.exists(path):
            messagebox.showwarning("Path Error", "The specified path does not exist.")
            return
        threading.Thread(target=download_thread, args=(url, path)).start()
    else:
        messagebox.showwarning("Input Error", "Please enter a valid YouTube URL and path.")

def download_thread(url, path):
    try:
        ydl_opts = {
            'progress_hooks': [progress_function],
            'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
            'format': 'bestvideo[height<=?1080]+bestaudio/best'
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {e}")

def progress_function(data):
    if data['status'] == 'downloading':
        if 'How Mr. Beast Became Successful on YouTube.f616.mp4' in data['filename']:
            if data.get('total_bytes') is not None:
                total_size = data['total_bytes']
                downloaded = data['downloaded_bytes']
                percentage = (downloaded / total_size) * 100
                progress_bar['value'] = percentage
                root.update_idletasks()
        elif 'How Mr. Beast Became Successful on YouTube.f251.webm' in data['filename']:
            if data.get('total_bytes') is not None:
                total_size = data['total_bytes']
                downloaded = data['downloaded_bytes']
                percentage = (downloaded / total_size) * 100
                progress_bar['value'] = percentage
                root.update_idletasks()
    elif data['status'] == 'finished':
        progress_bar['value'] = 0  # Reset progress bar for the next download

# Set up the GUI
root = tk.Tk()
root.title("YouTube Video Downloader")

tk.Label(root, text="Enter YouTube URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

tk.Label(root, text="Enter Download Path:").pack(pady=5)
path_entry = tk.Entry(root, width=50)
path_entry.pack(pady=5)

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=10)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=10)

root.mainloop()
