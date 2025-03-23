import os
import shutil

def copy_and_rename_files(base_dir, new_dir):
    # Walk through the base directory
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            # Construct the full file path
            full_file_path = os.path.join(root, file)
            
            # Get the relative path from the base directory and replace os separator with "-"
            relative_path = os.path.relpath(full_file_path, base_dir)
            new_file_name = relative_path.replace(os.sep, '-')
            
            # Construct the full new file path
            new_file_path = os.path.join(new_dir, new_file_name)
            
            # Ensure the new directory exists
            os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
            
            # Copy the file to the new directory with the new name
            shutil.copy2(full_file_path, new_file_path)
            print(f"Copied {full_file_path} to {new_file_path}")

# Example usage
base_dir = 'IDD_Detection/Annotations'
new_dir = 'IDD_Detection_post/annotation'
copy_and_rename_files(base_dir, new_dir)

ase_dir = 'IDD_Detection/JPEGImages'
new_dir = 'IDD_Detection_post/images'
copy_and_rename_files(base_dir, new_dir)
