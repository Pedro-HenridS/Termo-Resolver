def FilterCandidatesByCorrectPositions(correctPositionsCollections: dict, words: list):

    filtered = []

    for word in words:
        valid = True

        for position, letter in correctPositionsCollections.items():
            if word[position] != letter:
                valid = False
                break

        if valid:
            filtered.append(word)

    return filtered