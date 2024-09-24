from moviepy.editor import ImageSequenceClip, AudioFileClip, CompositeVideoClip

def add_background_music_to_slideshow(image_folder, audio_path, output_path, fps):
    import os
    images = [os.path.join(image_folder, img) for img in sorted(os.listdir(image_folder))]
    slideshow = ImageSequenceClip(images, fps=fps)
    audio = AudioFileClip(audio_path)
    video_with_music = slideshow.set_audio(audio)
    video_with_music.write_videofile(output_path)

# Example usage
add_background_music_to_slideshow('images/', 'background.mp3', 'slideshow_with_music.mp4', 1)
