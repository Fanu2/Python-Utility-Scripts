from moviepy.editor import VideoFileClip

def crop_video(input_path, output_path, crop_area):
    video = VideoFileClip(input_path)
    cropped_video = video.crop(x1=crop_area[0], y1=crop_area[1], x2=crop_area[2], y2=crop_area[3])
    cropped_video.write_videofile(output_path)

# Example usage
crop_video('input.mp4', 'output_cropped.mp4', (100, 100, 500, 500))
