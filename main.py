import yt_dlp
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

def download_playlist(playlist_url, download_path='.'):
    # yt-dlp options
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Best video with audio fallback
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',  # Save path
        'ignoreerrors': True,  # Skip errors and continue
        'quiet': False,  # Display detailed output
        'merge_output_format': 'mp4',  # Merge formats into mp4
        'noplaylist': False,  # Download entire playlist
        'postprocessors': [
            {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',  # Ensure video outputs as MP4
            },
        ],
        'verbose': True,  # Display verbose logs for debugging
    }

    # Download playlist using yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([playlist_url])
        except Exception as e:
            print(Fore.RED + f"[ERROR] Failed to download playlist: {e}")

# Example usage
if __name__ == '__main__':
    print(Fore.MAGENTA + '''
 __   __  _______  _______  ______  
|  | |  ||       ||       ||      | 
|  |_|  ||_     _||    _  ||  _    |
|       |  |   |  |   |_| || | |   |
|_     _|  |   |  |    ___|| |_|   |
  |   |    |   |  |   |    |       |
  |___|    |___|  |___|    |______| 

          - made by Ahmed Belmehnouf [ESTIN SRC]  
''')

    playlist_url = input(Fore.YELLOW + "[+] Enter the playlist URL: ")
    download_path = input(Fore.YELLOW + "[+] Enter the download path (default is current directory): ") or '.'

    print(Fore.GREEN + "[*] Starting download...")
    download_playlist(playlist_url, download_path)
    print(Fore.GREEN + "[*] Download completed.")
