from PIL import Image # pip install pillow (https://pypi.org/project/pillow/)
from rembg import remove  # pip install rembg (https://pypi.org/project/rembg/)
import os
import time

start_time = time.time()

def resize_images_in_directory(directory, max_width=800):
    for file_name in os.listdir(directory):
        if file_name.lower().endswith('.webp'):
            file_path = os.path.join(directory, file_name)
            file_output_path = os.path.join(directory, 'rembg_' + file_name)

            try:
                input = Image.open(file_path)
                output = remove(input)
                output.save(file_path)
                #os.remove(file_path)
                #print(f"Removed BG: {file_name}")

            except Exception as e:
                print(f"Error processing {file_name}: {e}")

# Usage
directory_path = os.getcwd()
resize_images_in_directory(directory_path)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
