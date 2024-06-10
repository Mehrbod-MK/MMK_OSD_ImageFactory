from .bmp import BMP
from .png import PNG
from .tga import TGA
from .tiff import TIFF

from .imageConverter import ImageConverter

class ImageFactory:
    def create_Image(self, name, width, height, *args):
        self.imageConvs_Classes = {
            "BMP": BMP,
            "PNG": PNG,
            "TGA": TGA,
            "TIFF": TIFF,
        }

        image_Class = self.imageConvs_Classes.get(name)
        return image_Class(name, width, height, *args)
    
    def convert_To(self, imageObject, destFormatName, *args):
        if(type(destFormatName) is not str):
            raise ValueError("ERROR CONVERT -> destFormatName must be a string.")
        
        targetImageObject = self.imageConvs_Classes.get(destFormatName)

        return targetImageObject(destFormatName, imageObject.width, imageObject.height, *args)


