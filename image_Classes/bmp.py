from .imageConverter import ImageConverter

class BMP(ImageConverter):
    def __init__(self, name, width, height, colorMixValue):
        if(colorMixValue < 0.0 or colorMixValue > 1.0):
            raise ValueError("ERROR -> BMP: ColorMixValue must be in range [0.0, 1.0].")
        
        super().__init__(name, width, height)
        self.colorMixValue = colorMixValue

    def getFinalFileSize(self):
        return self.width * self.height * self.colorMixValue
