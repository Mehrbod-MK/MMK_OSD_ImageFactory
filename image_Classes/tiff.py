import sys
from .imageConverter import ImageConverter

class TIFF(ImageConverter):
    def __init__(self, name, width, height, dpi, saveLayers, metas):
        super().__init__(name, width, height)
        if(dpi < 0):
            raise ValueError("ERROR -> TIFF: DPI Cannot be negative!")

        if(saveLayers != True or saveLayers != False):
            raise ValueError("ERROR -> TIFF: saveLayers must be a boolean!")
        
        if(type(metas) is not dict):
            raise ValueError("ERROR -> TIFF: Meta tags must be stored in a dictionary.")

        self.dpi = dpi
        self.saveLayers = saveLayers
        self.metas = metas

    def getFinalFileSize(self):
        finalValue = self.width * self.height * self.dpi * sys.getsizeof(self.metas)
        if(self.saveLayers):
            return finalValue + 10000
        else:
            return finalValue
        
    