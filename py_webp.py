import os
from PIL import Image

def convert_jpg_to_webp(input_folder, output_folder):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


    jpg_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.png'))]

    for jpg_file in jpg_files:

        jpg_path = os.path.join(input_folder, jpg_file)
        output_file = os.path.splitext(jpg_file)[0] + '.webp'
        output_path = os.path.join(output_folder, output_file)

        im = Image.open(jpg_path)
        im.save(output_path, 'WEBP')

if __name__ == "__main__":
    input_folder = r'C:\Users\Jesus\Desktop\webp\images'  
    output_folder = r'C:\Users\Jesus\Desktop\webp\newimages'
    convert_jpg_to_webp(input_folder, output_folder)