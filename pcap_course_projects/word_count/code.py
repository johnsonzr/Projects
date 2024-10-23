import re

def count_occurences(file_name, word):
    file = open(file_name)
    counter = 0
    content = file.read()
    words = re.split(r'[,\s.!]+', content)
    for string in words:
        if string.lower() == word:
            counter += 1
    return counter
print(count_occurences('first_text_file.txt', 'the'))