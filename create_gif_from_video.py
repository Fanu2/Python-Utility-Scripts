from moviepy.editor import VideoFileClip

def create_gif_from_video(video_path, output_path, start_time, end_time):
    video = VideoFileClip(video_path).subclip(start_time, end_time)
    video.write_gif(output_path)

# Example usage
create_gif_from_video('input.mp4', 'output.gif', 10, 20)
