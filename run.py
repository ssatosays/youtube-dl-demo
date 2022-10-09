from youtube_dl import YoutubeDL

target_list = [
    {"title": "Celebrate", "url": "https://www.youtube.com/watch?v=fMIn43MiwG8"}
]


def main():
    for e in target_list:
        title, url = e["title"], [e["url"]]
        options = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320'
            }],
            'outtmpl': f'downloads/{title}.%(ext)s'
        }
        with YoutubeDL(options) as ydl:
            result = ydl.download(url)
            assert result == 0


if __name__ == "__main__":
    main()
