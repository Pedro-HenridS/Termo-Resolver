def GetPositions(guesses, guessedWords):

    correctPositionsCollections = {}
    wrongPositiosCollections = {}

    for i, guess in enumerate(guesses.values()):
        for j, status in enumerate(guess):

            if status == 1:
                correctPositionsCollections[j] = guessedWords[i][j]

            elif status == -1:
                wrongPositiosCollections[j] = guessedWords[i][j]


    return (correctPositionsCollections, wrongPositiosCollections)