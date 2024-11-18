from pyzbar.pyzbar import decode
from PIL import Image

# Cambia 'your_image.png' por la ruta de tu imagen
image = Image.open('your_image.png')
decoded_objects = decode(image)

for obj in decoded_objects:
    print("Type:", obj.type)
    print("Data:", obj.data.decode('utf-8'))
