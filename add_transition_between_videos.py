from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.fx import fadein, fadeout

def add_transition(videos, output_path, transition_duration):
    clips = [fadein(fadeout(VideoFileClip(vid), transition_duration), transition_duration) for vid in videos]
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile(output_path)

# Example usage
add_transition(['video1.mp4', 'video2.mp4'], 'output_with_transition.mp4', 1)
