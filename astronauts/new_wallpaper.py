from PIL import Image, ImageFilter

image = Image.open('./astronauts/astro.jpg')
image.thumbnail((400, 400))
image.save('new_wallpaper.png', 'png')
print(image.size)
