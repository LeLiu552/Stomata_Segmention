import os
from ij import IJ
from ij.plugin import ZProjector

input_directory = ''
output_directory = ''

files_in_folder = os.listdir(input_directory)
print(files_in_folder)

# Filter the list to include only files ending with ".nd"
nd_files = [file for file in files_in_folder if file.endswith('.nd2')]

for file in nd_files:
    # Open the image, skip unsupported formats
    try:
        file_path = os.path.join(input_directory, file)

        # Check if file exists
        if not os.path.exists(file_path):
            print("File not found:", file_path)
            continue

        imp = IJ.openImage(file_path)
        if imp is None:
            print("Failed to open image:", file_path)
            continue
    except java.lang.IllegalArgumentException as e:
        print("Skipping unsupported format:", file, "-", e)
        continue

    imp = ZProjector.run(imp, "max")
    file_name = os.path.basename(file)
    output_path = os.path.join(output_directory, file_name.replace('.nd2', '.png'))
    IJ.saveAs(imp, "PNG", output_path)
