from moviepy.editor import VideoFileClip
from PIL import Image

def convert_frames_to_images(video_path, output_folder):
    video = VideoFileClip(video_path)
    for i, frame in enumerate(video.iter_frames()):
        img = Image.fromarray(frame)
        img.save(f"{output_folder}/frame_{i:04d}.png")

# Example usage
convert_frames_to_images('input.mp4', 'images/')
