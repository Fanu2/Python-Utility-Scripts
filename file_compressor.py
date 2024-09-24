import zipfile

def compress_file(file_path, output_path):
    with zipfile.ZipFile(output_path, 'w') as zipf:
        zipf.write(file_path, os.path.basename(file_path))

file_path = 'example.txt'
output_path = 'example.zip'
compress_file(file_path, output_path)
