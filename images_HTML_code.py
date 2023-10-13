import os
from PIL import Image

script_dir = os.path.dirname(__file__)
data_folder = os.path.join(script_dir, "data")
input_folder = os.path.join(data_folder, "images")
output_file = os.path.join(data_folder, "output.txt")

# Define the main HTML code template
main_template = '<p><img src="{0}" alt="{1}" width="700" height="{2}" /></p>'

# Read the path template from the template file
template_file_path = os.path.join(data_folder, "template.txt")

if not os.path.exists(template_file_path):
    print("Template file not found: %s" % template_file_path)
    exit()

with open(template_file_path, "r") as template_file:
    path_template = template_file.read().strip()

# Get a list of image files in the folder with JPG, JPEG, or PNG extensions
image_files = [f for f in os.listdir(input_folder) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

# Sort the image files based on their numeric names
image_files.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

with open(output_file, "w") as f:
    for i, image_file in enumerate(image_files, start=1):
        image_path = os.path.join(input_folder, image_file)
        with Image.open(image_path) as img:
            width, height = img.size
            proportional_height = int(700 * height / width)
            img_src = os.path.join(path_template, image_file)
            # Extract the name without the format (extension)
            image_name = os.path.splitext(image_file)[0]
            f.write(main_template.format(img_src, image_name, proportional_height))
            f.write('\n')

print("HTML file generated: %s" % output_file)
