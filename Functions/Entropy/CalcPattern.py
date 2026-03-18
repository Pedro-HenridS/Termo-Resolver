from collections import Counter


def CalcPattern(guess: str, target: str):
    pattern = [0] * len(guess)
    remaining_letters = Counter(target)

    for index, (guess_letter, target_letter) in enumerate(zip(guess, target)):
        if guess_letter == target_letter:
            pattern[index] = 1
            remaining_letters[guess_letter] -= 1

    for index, guess_letter in enumerate(guess):
        if pattern[index] == 1:
            continue

        if remaining_letters[guess_letter] > 0:
            pattern[index] = -1
            remaining_letters[guess_letter] -= 1

    return tuple(pattern)
