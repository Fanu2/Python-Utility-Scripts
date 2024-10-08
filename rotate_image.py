from PIL import Image

def rotate_image(input_path, output_path, angle):
    with Image.open(input_path) as img:
        rotated_img = img.rotate(angle, expand=True)
        rotated_img.save(output_path)

# Example usage
rotate_image('input.jpg', 'output_rotated.jpg', 45)
