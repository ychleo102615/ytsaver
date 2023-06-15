import speech_recognition as sr

def transcribe_audio(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)  # 讀取音訊檔案
    text = r.recognize_google(audio, language='zh-TW')  # 使用Google語音辨識API進行轉錄
    return text

if __name__ == "__main__":
    # # 呼叫語音辨識函式，並傳遞影片的音訊檔案路徑
    audio_file_path = input("audio file name:")
    transcribed_text = transcribe_audio(audio_file_path)
    print(transcribed_text)
