from moviepy.editor import VideoFileClip

def generate_thumbnail(video_path, output_path, time):
    video = VideoFileClip(video_path)
    frame = video.get_frame(time)
    from PIL import Image
    Image.fromarray(frame).save(output_path)

# Example usage
generate_thumbnail('input.mp4', 'thumbnail.jpg', 5)
