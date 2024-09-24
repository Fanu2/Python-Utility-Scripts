import os
import zipfile


def unzip_files_in_folder(folder_path):
    """
    Unzips all .zip files in the specified folder and renames folders if necessary to avoid overwriting.

    Args:
        folder_path (str): The path to the folder containing .zip files.
    """
    if not os.path.isdir(folder_path):
        raise ValueError(f"The directory {folder_path} does not exist.")

    # List all files in the folder
    files = [f for f in os.listdir(folder_path) if f.endswith('.zip')]

    for file in files:
        zip_file_path = os.path.join(folder_path, file)
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            # Determine extraction path
            extract_folder_name = os.path.splitext(file)[0]
            extract_folder_path = os.path.join(folder_path, extract_folder_name)

            # Check for conflicts and rename folder if necessary
            if os.path.exists(extract_folder_path):
                counter = 1
                new_extract_folder_path = f"{extract_folder_path}_{counter}"
                while os.path.exists(new_extract_folder_path):
                    counter += 1
                    new_extract_folder_path = f"{extract_folder_path}_{counter}"
                extract_folder_path = new_extract_folder_path

            # Extract the contents of the zip file
            zip_ref.extractall(extract_folder_path)
            print(f"Extracted {file} to {extract_folder_path}")


if __name__ == "__main__":
    # Set the directory path where .zip files are located
    folder_path = '/home/jasvir/Downloads/Facebook/'  # Update this path
    unzip_files_in_folder(folder_path)
