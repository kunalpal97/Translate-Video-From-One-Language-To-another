# 1 this part of the code used to extract the audio from the video
from moviepy.editor import *

clip1 = VideoFileClip("video_sample.mp4")

clip1.audio.write_audiofile("test_sample.mp3")


# 2 this is used to make the remove the audio from the video
# from moviepy.editor import *

# clip1 = VideoFileClip("videoclip.mp4")

# clip1 = clip1.without_audio()

# clip1.write_videofile("test_without_voice1.mp4")

# 3  here we can add the another audio file with other video
# from moviepy.editor import *
#
# video_file = VideoFileClip("test_w1.mp4")
#
# audio_file = AudioFileClip("test2.mp3")
#
# final_video = video_file.set_audio(audio_file)
# final_video.write_videofile("test_addedvoice.mp4")


