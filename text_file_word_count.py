def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    words = text.split()
    return len(words)

file_path = 'sample.txt'
word_count = count_words(file_path)
print(f'The file contains {word_count} words')
