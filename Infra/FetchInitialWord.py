import os
import random

def FetchInitialWord():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "database_5.txt")

    with open(file_path, "r", encoding="utf-8") as file:
        words = [w.strip() for w in file.readlines() if w.strip()]

    return random.choice(words)