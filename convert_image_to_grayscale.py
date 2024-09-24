from PIL import Image

def convert_to_grayscale(input_path, output_path):
    with Image.open(input_path) as img:
        grayscale_img = img.convert('L')
        grayscale_img.save(output_path)

# Example usage
convert_to_grayscale('input.jpg', 'output_grayscale.jpg')
