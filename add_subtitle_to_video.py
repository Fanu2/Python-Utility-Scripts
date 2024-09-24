from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def add_subtitle(video_path, subtitle_text, output_path):
    video = VideoFileClip(video_path)
    subtitle = TextClip(subtitle_text, fontsize=24, color='white', bg_color='black', size=video.size)
    subtitle = subtitle.set_position(('center', 'bottom')).set_duration(video.duration)
    video_with_subtitle = CompositeVideoClip([video, subtitle])
    video_with_subtitle.write_videofile(output_path)

# Example usage
add_subtitle('input.mp4', 'This is a subtitle', 'output_with_subtitle.mp4')
