from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def overlay_text_on_video(video_path, text, output_path):
    video = VideoFileClip(video_path)
    text_clip = TextClip(text, fontsize=24, color='white', bg_color='black', size=video.size)
    text_clip = text_clip.set_position(('center', 'bottom')).set_duration(video.duration)
    video_with_text = CompositeVideoClip([video, text_clip])
    video_with_text.write_videofile(output_path)

# Example usage
overlay_text_on_video('input.mp4', 'Overlay Text', 'output_with_text.mp4')
