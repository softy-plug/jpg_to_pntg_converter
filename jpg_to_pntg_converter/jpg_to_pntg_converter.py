import os
from PIL import Image

def convert_image(input_path, output_folder):
    with Image.open(input_path) as im:
        pntg_path = os.path.join(output_folder, os.path.splitext(os.path.basename(input_path))[0] + ".pntg")
        im.save(pntg_path, format="PNTG", quality=100)

def choose_folder(message):
    folder_path = input(message + "\nEnter the path to the folder: ")
    while not os.path.exists(folder_path):
        folder_path = input("The folder doesn't exist. Please enter a valid path to the folder: ")
    return folder_path

def main():
    print("Welcome to JPG to PNTG Converter!")
    jpg_folder = choose_folder("Enter the path to the folder containing the .jpg images:")
    pntg_folder = choose_folder("Enter the path to the output folder for the .pntg images:")
    # Create the output folder if it doesn't exist yet
    if not os.path.exists(pntg_folder):
        os.makedirs(pntg_folder)
    # Convert images
    for filename in os.listdir(jpg_folder):
        if filename.endswith('.jpg'):
            input_path = os.path.join(jpg_folder, filename)
            convert_image(input_path, pntg_folder)
    print("All images converted successfully to PNTG format and saved in the chosen folder!")

if __name__ == "__main__":
    main()

# softy_plug