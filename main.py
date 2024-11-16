import yt_dlp
from colorama import Fore, init

init()

def download_playlist(playlist_url, download_path='.'):
    ydl_opts = {
        'format': 'best',  # Download the best quality video/audio
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',  # Save the videos in the specified path
        'ignoreerrors': True,  # Continue even if some videos can't be downloaded
        'quiet': False,  # Show the download progress
        'extractaudio': False,  # Download videos as-is (you can set to True for audio-only)
        'noplaylist': False,  # Set to False to ensure entire playlist is downloaded
    }

    # Download playlist
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

# Example usage
if __name__ == '__main__': 
    print(Fore.MAGENTA +'''
 __   __  _______  _______  ______  
|  | |  ||       ||       ||      | 
|  |_|  ||_     _||    _  ||  _    |
|       |  |   |  |   |_| || | |   |
|_     _|  |   |  |    ___|| |_|   |
  |   |    |   |  |   |    |       |
  |___|    |___|  |___|    |______| 

          - made by ahmed belmehnouf [ESTIN SRC]  
''')
    
    playlist_url = input("[+] Enter the playlist URL: ")
    path = input("[/] Path: ")
    download_path = f"./{path}"  # Directory where you want to save the videos
    download_playlist(playlist_url, download_path)
