def CalcPattern(guess: str, target: str):
    pattern = []

    for i in range(len(guess)):
        if guess[i] == target[i]:
            pattern.append(1)
        else:
            pattern.append(0)

    return tuple(pattern)