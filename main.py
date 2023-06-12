import ytdownloader


if __name__ == "__main__":
    print("輸入youtube網址: ")
    # url = input()
    # url = "https://www.youtube.com/watch?v=OGLrYA8sEr4"
    # url = "https://www.youtube.com/watch?v=y6KMp5LJ9Do"
    url = "https://www.youtube.com/watch?v=6EmfiN3bi24"
    ytdownloader.download_youtube_video(url)
