from moviepy.editor import VideoFileClip
from moviepy.video.fx import gaussian_blur

def apply_gaussian_blur_to_video(input_path, output_path, radius):
    video = VideoFileClip(input_path)
    blurred_video = gaussian_blur(video, radius)
    blurred_video.write_videofile(output_path)

# Example usage
apply_gaussian_blur_to_video('input.mp4', 'output_blurred.mp4', 5)
