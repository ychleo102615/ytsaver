import os
import speech_recognition as sr
import shutil
from pydub import AudioSegment
from pydub.silence import split_on_silence

def transcribe_audio(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)  # 讀取音訊檔案
    text = r.recognize_google(audio, language='zh-TW')  # 使用Google語音辨識API進行轉錄
    return text

# https://www.geeksforgeeks.org/python-speech-recognition-on-large-audio-files/
def transcribe_audio_file(audio_file_path):
    # 參考來源
    song = AudioSegment.from_wav(audio_file_path)

    # open a file where we will concatenate
    # and store the recognized text
    fh = open("recognized.txt", "w+")
    print("Open recognized.txt")

    text = ""

    print("Splitting Audio...")
    chunks = split_on_silence(song,
        # must be silent for at least 0.5 seconds
        # or 500 ms. adjust this value based on user
        # requirement. if the speaker stays silent for
        # longer, increase this value. else, decrease it.
        min_silence_len = 500,

        # consider it silent if quieter than -16 dBFS
        # adjust this per requirement
        # silence_thresh = -16
        silence_thresh = -42
    )

    # create a directory to store the audio chunks.
    try:
        os.mkdir('audio_chunks')
    except(FileExistsError):
        pass

    # move into the directory to
    # store the audio files.
    os.chdir('audio_chunks')

    print("chunk size: " + str(len(chunks)))
    i = 0
    # process each chunk
    for chunk in chunks:

        # Create 0.5 seconds silence chunk
        chunk_silent = AudioSegment.silent(duration = 10)

        # add 0.5 sec silence to beginning and
        # end of audio chunk. This is done so that
        # it doesn't seem abruptly sliced.
        audio_chunk = chunk_silent + chunk + chunk_silent

        # export audio chunk and save it in
        # the current directory.
        print("Saving chunk{0}.wav".format(i))
        # specify the bitrate to be 192 k
        audio_chunk.export("./chunk{0}.wav".format(i), bitrate ='192k', format ="wav")

        # the name of the newly created chunk
        filename = 'chunk'+str(i)+'.wav'

        print("Processing chunk "+str(i))

        # get the name of the newly created chunk
        # in the AUDIO_FILE variable for later use.
        file = filename

        # create a speech recognition object
        r = sr.Recognizer()

        # recognize the chunk
        with sr.AudioFile(file) as source:
            # remove this if it is not working
            # correctly.
            r.adjust_for_ambient_noise(source)
            audio_listened = r.record(source)
            # audio_listened = r.listen(source)

        try:
            # try converting it to text
            rec = r.recognize_google(audio_listened, language='zh-TW')
            # write the output to the file.
            # print("i: " + str(rec))
            print("Recognizing chunk " + str(i) + " ...")
            fh.write(str(rec) + "\n")
            text = text + str(rec) + "\n"

        # catch any errors.
        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError as e:
            print("Could not request results. check your internet connection")

        i += 1

    os.chdir('..')
    shutil.rmtree('audio_chunks', ignore_errors=True)

    return text

def main():
    import sys
    # # 呼叫語音辨識函式，並傳遞影片的音訊檔案路徑
    if len(sys.argv) < 2:
        print("No audio file specified.")
        return
    audio_file_path = sys.argv[1]
    transcribe_audio_file(audio_file_path)

if __name__ == "__main__":
    main()
