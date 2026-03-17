from collections import Counter

def VerifyAnswer(word, dayWord):
    viewResult = [None] * len(word)
    guessVerify = [None] * len(word)
    wrongLetters = []
    lettersCount = Counter() #Pedro, esse contador basicamente diz a quantidade de letras certas 
                             # ou meio certas que cada letra da palavra tem

    dayWordLettersCount = Counter(dayWord)

    for i, (letter, dayLetter) in enumerate(zip(word, dayWord)):
        if letter == dayLetter:
            viewResult[i] = "✅ " + letter
            guessVerify[i] = 1
            dayWordLettersCount[letter] -= 1
            lettersCount += Counter(letter)

    for i, letter in enumerate(word):
        if guessVerify[i] == 1:
            continue

        if dayWordLettersCount[letter] > 0:
            viewResult[i] = "🟨 " + letter
            guessVerify[i] = -1
            dayWordLettersCount[letter] -= 1
            lettersCount += Counter(letter)
        else:
            viewResult[i] = "🟥 " + letter
            guessVerify[i] = 0
            wrongLetters.append(letter)
        

    return (viewResult, guessVerify, wrongLetters, lettersCount)