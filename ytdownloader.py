import youtube_dl

FILE_TYPE = "wav"
# FILE_TYPE = "mp3"

def download_youtube_audio(url):
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
                'preferredcodec': FILE_TYPE,
                'preferredquality': '192',
                }]
            }
    with youtube_dl.YoutubeDL(audio_opts) as ydl:
        # ydl.download([url])
        result = ydl.extract_info(url)
        print(type(result))
        if type(result) is not dict:
            # print("not dict")
            return
        title = result.get("title")
        if title is None:
            # print("is None")
            return
        return str(title) + "." + FILE_TYPE
