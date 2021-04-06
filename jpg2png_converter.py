import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

#to check if output_folder exist or not

if not os.path.exists(output_folder):
    os.mkdir(output_folder)


for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}\{filename}")
    img.save(f"{output_folder}\{filename}")