"""This file creates meme."""
from PIL import Image, ImageDraw, ImageFont


class memeGenerator:
    """This class creates meme."""

    def __init__(self, output_dir):
        """Output directory creation."""
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500):
        """Meme creation."""
        img = Image.open(img_path)
        if img.width > width:
            new_width = width
            new_height = img.height*width/img.width
            img = img.resize((new_width, new_height))
        draw = ImageDraw.Draw(img)
        fnt = ImageFont.truetype("arial.ttf", 24)
        draw.text((10, 30), f'{text} - {author}', font=fnt, fill='white')
        img.save(self.output_dir)
        return self.output_dir
