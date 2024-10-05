from moviepy.editor import *

main_video = VideoFileClip("test_without_voice1.mp4")  #.subclip(10,33)
main_video = main_video.without_audio()

main_audio = AudioFileClip("test_to_audio.mp3")

final_video = main_video.set_audio(main_audio)

final_video.write_videofile("finalvideo.mp4")