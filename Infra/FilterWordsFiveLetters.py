import os

def FilterWordsFiveLetters():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "database.txt")

    with open(file_path, "r", encoding="utf-8") as file:
        words = file.readlines()

    filtered_words = [w.strip() for w in words if len(w.strip()) == 5]

    output_path = os.path.join(base_path, "database_5.txt")

    with open(output_path, "w", encoding="utf-8") as file:
        file.write("\n".join(filtered_words))


FilterWordsFiveLetters()