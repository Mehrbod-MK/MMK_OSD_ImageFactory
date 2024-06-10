from .bmp import BMP
from .png import PNG
from .tga import TGA
from .tiff import TIFF

class ImageFactory:
    def create_Image(self, name, width, height, *args):
        self.imageConvs_Classes = {
            "BPM": BMP,
            "PNG": PNG,
            "TGA": TGA,
            "TIFF": TIFF,
        }

        image_Class = self.imageConvs_Classes.get(name)
        return image_Class(name, width, height, *args)

