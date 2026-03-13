from collections import Counter

def VerifyAnswer(word, dayWord):
    
    correctSpace = [None] * len(word)
    wrongLetters = []
    dayWordLettersCount = Counter(dayWord)

    for i, (letter, dayLetter) in enumerate(zip(word, dayWord)):
        if letter == dayLetter:
            correctSpace[i] = "✅ " + letter

        elif letter != dayLetter and letter in dayWord and dayWordLettersCount[letter] > 0:
            correctSpace[i] = "🟨 " + letter
            dayWordLettersCount[letter] -= 1

        else:
            correctSpace[i] = "🟥 " + letter
            wrongLetters.append(correctSpace[i])

    return (correctSpace, wrongLetters)
