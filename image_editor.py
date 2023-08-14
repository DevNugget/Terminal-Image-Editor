from PIL import Image, ImageFilter
import os


#image = Image.open("./shrek.jpg")
#print(image.format, image.size, image.mode)

#image = image.transpose(Image.Transpose.ROTATE_90)
#image = image.filter(ImageFilter.BoxBlur(4))

#image.save("shrekcrop.jpg")


print("Image Editor")
print("--------------")
print("1. Directory")
print("2. Single File")
print("")

editor_mode = int(input("Select Mode >> "))

if editor_mode == 2:
    file_path = input("File Path >> ")
    image = Image.open(file_path)

    print("")
    print("Loaded image:")
    print(f"FORMAT: {image.format}")
    print(f"SIZE: {image.size}")
    print(f"MODE: {image.mode}")

    print("Action")
    print("--------------")
    print("1. Filter")
    print("2. Enhance")
    print("3. Save & Exit")
    print("")
    edit_option = int(input("Select Edit >> "))

    if edit_option == 1:
        print("Filters")
        print("")
        print("1. Box Blur")
        print("2. Gaussian Blur")
        print("3. Sharpen")

