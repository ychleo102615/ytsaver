import ytdownloader
import transcriber

def main():
    print("輸入youtube網址: ")
    # url = input()
    # url = "https://www.youtube.com/watch?v=OGLrYA8sEr4"
    # url = "https://www.youtube.com/watch?v=y6KMp5LJ9Do"
    url = "https://www.youtube.com/watch?v=JJn2rE8OHII"
    audio_file = ytdownloader.download_youtube_audio(url)
    print(audio_file)
    print(type( audio_file ))
    if not isinstance(audio_file, str):
        print("the result of download lacks title ")
        return

    transcribed_text = transcriber.transcribe_audio(audio_file)
    print(transcribed_text[:100])

if __name__ == "__main__":
    main()
