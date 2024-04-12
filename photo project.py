from PIL import Image, ImageFilter

with Image.open("cat.png") as original:
    # #გაშავთეთრება
    # picture_gray = original.convert("L")
    #ფოტოს გაბუნდოვნება
    # picture_blur = original.filter(ImageFilter.BLUR)
    photo_rotate = original.transpose(Image.ROTATE_90)

    #ფოტოს გახსნა
    # picture_blur.show()
    # #ფოტოს შენახვა
    # picture_gray.save("black_chicken.png")
    photo_rotate.show()


    # original.show()
    # print(original.size)
    # print(original.format)
    # print(original.mode)