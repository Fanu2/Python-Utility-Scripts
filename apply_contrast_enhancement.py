from PIL import Image, ImageEnhance

def apply_contrast(input_path, output_path, factor):
    with Image.open(input_path) as img:
        enhancer = ImageEnhance.Contrast(img)
        img_enhanced = enhancer.enhance(factor)
        img_enhanced.save(output_path)

# Example usage
apply_contrast('input.jpg', 'output_contrast.jpg', 2)
