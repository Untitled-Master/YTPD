# YTPD - YouTube Playlist Downloader

YTPD is a simple Python script for downloading entire YouTube playlists using `yt-dlp`. It allows you to download videos in the best available quality and saves them in a specified directory.

## Features

- Download entire YouTube playlists.
- Saves videos in the best quality.
- Option to specify the download path.
- Handles errors gracefully and continues downloading other videos even if some fail.
- Can be customized to download audio only by setting `'extractaudio': True`.

## Prerequisites

Before running the script, ensure you have the following:

- Python 3.x installed on your machine.
- `yt-dlp` library installed.
- `colorama` library installed.

You can install the required libraries using pip:

```bash
pip install yt-dlp colorama
```

## How to Use

1. Clone the repository:

```bash
git clone https://github.com/Untitled-Master/YTPD.git
cd YTPD
```

2. Run the script:

```bash
python ytpd.py
```

3. The script will ask for the following inputs:
   - **Playlist URL**: Enter the URL of the YouTube playlist you want to download.
   - **Path**: Specify the directory where you want to save the videos.

4. The script will start downloading the videos in the best available quality and save them in the specified directory.

## Example Usage

```bash
$ python ytpd.py

[+] Enter the playlist URL: https://www.youtube.com/playlist?list=PL5e6Wlg7lEdaIKpVwACVfA4_8QeERpQFh
[/] Path: Downloads
```

This will download the entire playlist into a folder called `Downloads` in the current directory.

## Notes

- The script will save the videos with the same title as they appear on YouTube.
- You can modify the script to change the output format, handle audio-only downloads, or further customize it.
- You can always check for updates to `yt-dlp` to get the latest features and improvements.

## License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Author

Made by **Ahmed Belmehnouf** from **ESTIN SRC**.
