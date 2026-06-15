import os

# Write the folder path whose contents you want to print
directory_path = r"C:\Users\ANKITSAINI\OneDrive\Documents\python-practice"

# Check whether the directory exists or not
if os.path.exists(directory_path):
    print("Directory contents:\n")

    # Print all files and folders inside the directory
    for item in os.listdir(directory_path):
        print(item)
else:
    print("Error: This directory path does not exist.")