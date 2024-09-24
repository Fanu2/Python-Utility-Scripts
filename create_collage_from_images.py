from PIL import Image

def create_collage(image_paths, collage_path, size):
    images = [Image.open(img).resize(size) for img in image_paths]
    collage = Image.new('RGB', (size[0] * len(images), size[1]))
    for i, img in enumerate(images):
        collage.paste(img, (i * size[0], 0))
    collage.save(collage_path)

# Example usage
create_collage(['img1.jpg', 'img2.jpg'], 'collage.jpg', (300, 200))
