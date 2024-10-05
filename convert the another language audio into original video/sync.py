import moviepy.editor as mp
import speech_recognition as sr
import numpy as np

# Video file path
video_path = 'test_sample.mp3'

# Load the video using moviepy
video = mp.VideoFileClip(video_path)

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Variable to store the start time
start_time = None

# Extract audio from the video
audio = video.audio.to_soundarray()

# Calculate the frame rate of the audio
audio_frame_rate = audio.shape[0] / video.duration

# Set sample width to 2 bytes (16 bits)
sample_width = 2

for i, frame in enumerate(video.iter_frames(fps=video.fps)):
    # Check if the start time is not recorded yet
    if start_time is None:
        # Record the start time
        start_time = i / video.fps

    # Convert the frame to grayscale for speech recognition
    # (Note: You may need to adjust this depending on your use case)
    gray_frame = frame

    # Calculate the corresponding audio frame for this video frame
    audio_frame = int(i * audio_frame_rate / video.fps)

    # Perform speech recognition on the audio frame
    audio_chunk = audio[audio_frame:audio_frame + int(audio_frame_rate / video.fps)]
    recognizer.adjust_for_ambient_noise(audio_chunk, duration=0.5)
    try:
        text = recognizer.recognize_google(audio_chunk, sample_rate=audio_frame_rate)
        if text:
            break
    except sr.UnknownValueError:
        pass

# Calculate the total time
if start_time is not None:
    print(f"Total time from video start to first human voice: {start_time:.2f} seconds")
else:
    print("No audio with human voice detected in the video.")
