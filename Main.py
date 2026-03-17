from Functions.VerifyAnswer import VerifyAnswer
from Functions.GetPositions import GetPositions
from Functions.Filters.FilterCandidates import FilterCandidatesByWrongLetters
from Functions.Filters.FilterCandidatesByCorrectPositions import FilterCandidatesByCorrectPositions
from Functions.Filters.FilterCandidatesByWrongPositions import FilterCandidatesByWrongPositions
from Functions.Filters.FilterCandidatesByAbscense import FilterCandidatesByAbscense
from Functions.Entropy.CalcEntropies import CalcEntropies
from Infra.FetchInitialWord import FetchInitialWord
from Infra.FetchAllWords import FetchAllWords
from collections import Counter


def main():

    word = FetchInitialWord()
    candidates = FetchAllWords()
    guesses = {}
    viewGuesses = {}
    allWrongLetters = []
    guessedWords = []
    lettersCount = Counter() #necessario pra função wrongPosition atualizada
    

    

    for i in range(10):
        guess = input("Insira sua tentativa [5 letras]: ")
        if (guess in candidates) and (guess != word):
            candidates.remove(guess)

        guessedWords.append(guess)
        viewTemplate, guessTemplate, wrongLetters, lettersCount = VerifyAnswer(guess, word)

        guesses[i] = guessTemplate
        viewGuesses[i] = viewTemplate

        allWrongLetters.extend(x for x in wrongLetters if x not in allWrongLetters)

        for i in range(len(viewGuesses)):
            print(*viewGuesses[i])

        correctPositions, wrongPositions = GetPositions(guesses, guessedWords)

        #Filters 
        #candidates = FilterCandidatesByWrongLetters(candidates, allWrongLetters)
        #Não precisa mais do WrongLetters pq agr a WrongPosition faz os dois ao mesmo tempo (por conhecidencia)
        print("correctPositions:", correctPositions)
        print("wrongPositions:", wrongPositions)
        print("wrongLetters atual:", wrongLetters)
        print("lettersCount atual:", lettersCount)
        
        candidates = FilterCandidatesByCorrectPositions(correctPositions, candidates)
        candidates = FilterCandidatesByWrongPositions(wrongPositions, candidates, wrongLetters, lettersCount)
        print("Canditados: ", candidates)
        #candidates = FilterCandidatesByAbscense(wrongPositions, candidates)
        #Nao entendi o que essa função de cima faz, o programa roda dboa sem ela.
        
        if(i >= 1):
            entropies = CalcEntropies(candidates)
            bestWord = max(entropies, key=entropies.get)

            print("Palavra sugerida:", bestWord)
        
    print("Palavra correta: ", word)

    return 0

if __name__ == "__main__":
    main()