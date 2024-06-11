from PIL import Image, ImageChops

def resize_image(img, size=(100, 100)):
    # img = Image.open(image_path)
    img_resized = img.resize(size, Image.Resampling.LANCZOS)
    return img_resized

def trim_image(img):
    bg = Image.new(img.mode, img.size, img.getpixel((0,0)))
    diff = ImageChops.difference(img, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        img = img.crop(bbox)

    return img

def trim_and_resize_image(image_path, size=(100, 100)):
    img = Image.open(image_path)
    img_trimed = trim_image(img)
    img_trim_and_resized = resize_image(img_trimed, size)
    return img_trim_and_resized
    