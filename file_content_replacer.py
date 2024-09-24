def replace_text_in_file(file_path, old_text, new_text):
    with open(file_path, 'r') as file:
        content = file.read()

    content = content.replace(old_text, new_text)

    with open(file_path, 'w') as file:
        file.write(content)

file_path = 'example.txt'
replace_text_in_file(file_path, 'old_text', 'new_text')
