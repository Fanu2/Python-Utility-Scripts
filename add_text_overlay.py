from PIL import Image, ImageDraw, ImageFont

def add_text_overlay(input_path, output_path, text, position, font_size):
    with Image.open(input_path) as img:
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", font_size)
        draw.text(position, text, font=font, fill='white')
        img.save(output_path)

# Example usage
add_text_overlay('input.jpg', 'output_with_text.jpg', 'Hello!', (10, 10), 50)
