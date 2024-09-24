from pytube import YouTube

def download_video(url, path):
    yt = YouTube(url)
    ys = yt.streams.get_highest_resolution()
    ys.download(path)

video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
download_video(video_url, '/path/to/download')
