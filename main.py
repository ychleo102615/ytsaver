import ytdownloader
import transcriber
import gpt_adapter

def main():
    print("輸入youtube網址: ")
    url = input()

    audio_file = ytdownloader.download_youtube_audio(url)

    assert isinstance(audio_file, str), "下載音訊檔發生問題。"

    transcribed_text = transcriber.transcribe_audio_file(audio_file)

    # result = gpt_adapter.generate(transcribed_text)
    # print(result)

if __name__ == "__main__":
    main()
