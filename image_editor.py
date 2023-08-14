from PIL import Image, ImageFilter, ImageEnchance
import os


image = Image.open("./shrek.jpg")
print(image.format, image.size, image.mode)

#image = image.transpose(Image.Transpose.ROTATE_90)
image = image.filter(ImageFilter.BoxBlur(4))

image.save("shrekcrop.jpg")