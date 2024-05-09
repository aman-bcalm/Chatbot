import os

def get_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
        for d in dirnames:
            dp = os.path.join(dirpath, d)
            total_size += get_size(dp)
    return total_size

def display_size(start_path='.'):
    print("Size of each subfolder and file:")
    for dirpath, dirnames, filenames in os.walk(start_path):
        folder_size = 0
        for f in filenames:
            fp = os.path.join(dirpath, f)
            folder_size += os.path.getsize(fp)
        for d in dirnames:
            dp = os.path.join(dirpath, d)
            folder_size += get_size(dp)
        print(f"{dirpath} - {folder_size} bytes")

# Get the current directory
current_directory = os.getcwd()
display_size(current_directory)