from PIL import Image

def convert_to_grayscale(image_path, output_path):
    with Image.open(image_path) as img:
        gray_img = img.convert('L')
        gray_img.save(output_path)

convert_to_grayscale('input.jpg', 'grayscale.jpg')
