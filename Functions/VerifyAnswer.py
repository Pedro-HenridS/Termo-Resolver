from collections import Counter

def VerifyAnswer(word: str, dayWord: str):

    """
    Verifica uma tentativa de palavra no jogo Termo.

    Args:
        word (str): Palavra tentada pelo jogador.
        dayWord (str): Palavra correta do dia.

    Returns:
        tuple:
            correctSpace (list):
                Lista indicando o resultado visual de cada letra
                ("🟩", "🟨", "🟥").

            correctSpaceNumeric (list):
                Lista numérica com o resultado de cada letra
                0  = letra incorreta
                1  = letra correta
                -1 = letra correta na posição errada

            wrongLetters (list):
                Lista de letras que não existem na palavra do dia.
    """
    
    viewResult = [None] * len(word)
    guessVerify = [None] * len(word)
    wrongLetters = []
    dayWordLettersCount = Counter(dayWord)

    for i, (letter, dayLetter) in enumerate(zip(word, dayWord)):
        if letter == dayLetter:
            viewResult[i] = "✅ " + letter
            guessVerify[i] = 1

        elif letter != dayLetter and letter in dayWord and dayWordLettersCount[letter] > 0:
            viewResult[i] = "🟨 " + letter
            guessVerify[i] = -1
            dayWordLettersCount[letter] -= 1

        else:
            viewResult[i] = "🟥 " + letter
            guessVerify[i] = 0
            wrongLetters.append(letter)

    return (viewResult, guessVerify, wrongLetters)
