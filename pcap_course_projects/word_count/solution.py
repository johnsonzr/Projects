def count_occurences(file_name, word):
    count = 0
    try:
        stream = open(file_name, 'r')
        for line in stream:
            words = line.replace('.', ' ').replace(',', ' ').split()
            for i in words:
                if(i.lower() == word.lower()):
                    count = count + 1
    except Exception:
        print('something went wrong')
    finally:
        stream.close()
    return count