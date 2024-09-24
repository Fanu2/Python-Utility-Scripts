from moviepy.editor import VideoFileClip

def split_video_into_clips(video_path, clip_duration, output_folder):
    video = VideoFileClip(video_path)
    duration = int(video.duration)
    for start_time in range(0, duration, clip_duration):
        end_time = min(start_time + clip_duration, duration)
        clip = video.subclip(start_time, end_time)
        clip.write_videofile(f"{output_folder}/clip_{start_time}.mp4")

# Example usage
split_video_into_clips('input.mp4', 10, 'clips/')
