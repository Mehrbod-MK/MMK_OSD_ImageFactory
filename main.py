from image_Classes.ImageConverterFactory import ImageFactory

imageFactory = ImageFactory()

img_BMP = imageFactory.create_Image('BMP', 640, 480, 0.5)
print(f"BMP Image Size:  {img_BMP.getFinalFileSize()} bytes.")

img_PNG = imageFactory.create_Image('PNG', 800, 600, 80, False)
print(f"PNG Image Size:  {img_PNG.getFinalFileSize()} bytes.")

img_TGA = imageFactory.create_Image('TGA', 400, 300, True, 7)
print(f"TGA Image Size:  {img_TGA.getFinalFileSize()} bytes.")

img_TIFF = imageFactory.create_Image('TIFF', 1024, 768, 300, False, {'Author': 'Mehrbod Molla Kazemi','Professor': 'Dr. Pourya Khanzadi'})
print(f"TIFF Image Size:  {img_TIFF.getFinalFileSize()} bytes.")

img_Convert_TIFF_To_BMP = imageFactory.convert_To(img_TIFF, "BMP", 0.2)
print(f"Converted image from TIFF to BMP Size:  {img_Convert_TIFF_To_BMP.getFinalFileSize()} bytes.")
