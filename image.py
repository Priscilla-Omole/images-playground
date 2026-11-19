from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
# filtered_image = img.filter(ImageFilter.SHARPEN)
# filtered_image.save("sharpened.png", "png")

filtered_image = img.convert('L')
rotated_file = filtered_image.rotate(90)
resize_file = filtered_image.resize((300, 300))
rotated_file.save('grey.png', 'png')
resize_file.save('resized_pikachu.png', 'png')
rotated_file.show()
