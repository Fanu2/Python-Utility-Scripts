from PIL import Image

def add_logo_watermark(image_path, logo_path, output_path, position):
    with Image.open(image_path) as img:
        with Image.open(logo_path) as logo:
            img.paste(logo, position, logo)
            img.save(output_path)

# Example usage
add_logo_watermark('input.jpg', 'logo.png', 'output_with_logo.jpg', (0, 0))
