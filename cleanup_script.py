import os
import shutil
import glob

# Function to delete files in a specific folder
def delete_files_in_folder(folder_path, pattern="*"):
    try:
        # Create the full path with the given pattern
        full_path = os.path.join(folder_path, pattern)
        
        # Use glob to get all files matching the pattern
        files = glob.glob(full_path)
        
        # Delete each file
        for file in files:
            try:
                if os.path.isfile(file):
                    os.remove(file)
                    print(f"Deleted file: {file}")
                elif os.path.isdir(file):
                    shutil.rmtree(file)
                    print(f"Deleted directory: {file}")
            except Exception as e:
                print(f"Error deleting {file}: {e}")
    except Exception as e:
        print(f"Error accessing {folder_path}: {e}")

# Paths you specified
temp_folder = r"C:\Windows\Temp"
user_temp_folder = r"C:\Users\evagh\AppData\Local\Temp"
prefetch_folder = r"C:\Windows\Prefetch"

# Perform the cleanup on each directory
delete_files_in_folder(temp_folder)
delete_files_in_folder(user_temp_folder)
delete_files_in_folder(prefetch_folder)

print("File cleanup completed.")
