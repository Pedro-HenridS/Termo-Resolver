def FilterCandidatesByWrongLetters(candidates, wrongLetters):

    candidatesCopy = [
        word for word in candidates
        if not any(letter in word for letter in wrongLetters)
    ]


    return candidatesCopy

