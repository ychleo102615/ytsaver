import youtube_dl

def download_youtube_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s',
        # 'outtmpl': '%(id)s.%(ext)s',
    }

    audio_opts = {
            'format': 'bestaudio/best',
            # 'format': 'mp3', # invalid
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
                # 'progress_hooks': [get_filename]
                }]
            }
    with youtube_dl.YoutubeDL(audio_opts) as ydl:
    # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        # print(ydl.extract_info(url))

