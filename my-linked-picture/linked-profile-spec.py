from PIL import Image, ImageFilter

image = Image.open('./my-linked-picture/Priscilla.jpeg')
image.thumbnail((400, 400))
image.save('updated_image.png', 'png')
