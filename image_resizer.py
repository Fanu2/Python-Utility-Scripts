from PIL import Image

input_image_path = 'input.jpg'
output_image_path = 'output.jpg'

with Image.open(input_image_path) as img:
    img = img.resize((800, 600))
    img.save(output_image_path)
