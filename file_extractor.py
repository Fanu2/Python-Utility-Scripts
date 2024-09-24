import zipfile

def extract_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

zip_path = 'example.zip'
extract_to = 'extracted_files'
extract_file(zip_path, extract_to)
