from moviepy.editor import VideoFileClip
from PIL import Image

def extract_frames_at_interval(video_path, output_folder, interval):
    video = VideoFileClip(video_path)
    for t in range(0, int(video.duration), interval):
        frame = video.get_frame(t)
        Image.fromarray(frame).save(f"{output_folder}/frame_{t}.png")

# Example usage
extract_frames_at_interval('input.mp4', 'frames/', 10)
