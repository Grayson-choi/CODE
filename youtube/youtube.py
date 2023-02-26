import os
import pytube # pip install pytube
from pytube.cli import on_progress
from moviepy.editor import *

# 유튜브 영상 편집
# https://zulko.github.io/moviepy/install.html

def make_youtube_clip(file, start, *end):
    # Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
    clip = VideoFileClip(file).subclip(start)

    # Reduce the audio volume (volume x 0.8)
    # clip = clip.volumex(0.8)

    # Generate a text clip. You can customize the font, color, etc.
    # txt_clip = TextClip("My Holidays 2013",fontsize=70,color='white')

    # Say that you want it to appear 10s at the center of the screen
    # txt_clip = txt_clip.set_pos('center').set_duration(10)

    # Overlay the text clip on the first video clip
    video = CompositeVideoClip([clip])

    # Write the result to a file (many options available !)
    video.write_videofile(f"downloads/{file}_clip.mp4")

file_list = os.listdir("./downloads")

folder = "./downloads"
for file in file_list:
    # if "lovers" in file:
        # make_youtube_clip(f"{folder}/{file}", 30)
    if "Saint" in file:
        make_youtube_clip(f"{folder}/{file}", 11)

        


# url = "https://youtu.be/STGe54blV_0"
url_list = [
    "https://youtu.be/F1RevEIZ0Vs", 
    "https://youtu.be/STGe54blV_0",
    "https://youtu.be/Z-R3wV7kGeY",
]


def download_youtube_video(url_list):
    for url in url_list:
        yt = pytube.YouTube(url, on_progress_callback=on_progress)
        print(yt.streams)

        save_dir = "./downloads" # 저장경로

        yt.streams.filter(progressive=True, file_extension="mp4")\
            .order_by("resolution")\
            .desc()\
            .first()\
            .download(save_dir)
    
