from PIL import Image

def create_blank_image(width, height):
    return Image.new("1", (width, height), color=1)