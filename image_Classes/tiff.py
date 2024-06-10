from .imageConverter import ImageConverter

class TIFF(ImageConverter):
    def __init__(self, name, width, height, dpi, saveLayers, metas):
        super().__init__(name, width, height)
        if(dpi < 0):
            raise ValueError("ERROR -> PNG: DPI Cannot be negative!")

        if(isInterlaced != True or isInterlaced != False):
            raise ValueError("ERROR -> PNG: IsInterlaced must be a boolean!")

        self.dpi = dpi
        self.isInterlaced = isInterlaced

    def getFinalFileSize(self):
        finalValue = self.width * self.height * self.dpi
        if(self.isInterlaced):
            return finalValue / 2.0
        else:
            return finalValue
        
    