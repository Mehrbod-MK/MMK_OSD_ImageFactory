from .imageConverter import ImageConverter

class TGA(ImageConverter):
    def __init__(self, name, width, height, isAtlas, numPages):
        #if(isAtlas != True or isAtlas != False):
        #    raise ValueError("ERROR -> TGA: isAtlas must be a boolean!")
        if(type(numPages) is not int):
            raise ValueError("ERROR -> TGA: numPages must be an integer!")
        
        super().__init__(name, width, height)
        self.isAtlas = isAtlas
        self.numPages = numPages

    def getFinalFileSize(self):
        if(self.isAtlas):
            return self.width * self.height * self.numPages
        else:
            return self.width * self.height
