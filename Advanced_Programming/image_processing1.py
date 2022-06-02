# JPEG to PNG converter
from PIL import Image
import sys
import os
import re

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not (os.path.exists(image_folder)):
    raise("Image Folder Not Found")

if not (os.path.exists(output_folder)):
    os.makedirs(output_folder)

for file in os.listdir(image_folder):
    file_to_process = image_folder + "\\\\" + file
    img = Image.open(file_to_process)
    clean_name = (os.path.splitext(file))[0]
    file_to_save = output_folder + "\\\\" + clean_name + ".png"
    img.save(file_to_save, "png")
