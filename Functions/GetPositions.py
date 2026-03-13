def GetPositions(guesses, guessedWords):

    correctPositioned = [None] * 5
    wrongPositioned = []

    for i, guess in enumerate(guesses.values()):
        for j, status in enumerate(guess):

            if status == 1:
                correctPositioned[j] = guessedWords[i][j]

            elif status == -1:
                wrongPositioned.append(guessedWords[i][j])

    print(correctPositioned)
    print(wrongPositioned)