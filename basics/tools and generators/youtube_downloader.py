from pytube import YouTube

SAVE_PATH = "C:/temp"


def download_youtube_video():
    link = input("Enter the URL of the YouTube Video\n")
    try:
        youtube = YouTube(link)
    except:
        print("The video could not be reached.")
    print("Information about the video:")
    print("Title:", youtube.title)
    print("Views:", youtube.views)
    d_video = youtube.streams.get_highest_resolution()
    print("The download of the video begins")
    try:
        d_video.download(SAVE_PATH)
    except:
        print("An error has occurred!")
    print("Download was successful!")
    download_youtube_video()


download_youtube_video()
