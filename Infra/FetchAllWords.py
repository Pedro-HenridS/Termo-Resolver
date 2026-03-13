import os

def FetchAllWords():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "database_5.txt")

    words = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            word = line.strip()
            if word:
                words.append(word)

    return words