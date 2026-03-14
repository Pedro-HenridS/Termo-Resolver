from Functions.VerifyAnswer import VerifyAnswer
from Functions.GetPositions import GetPositions
from Functions.Filters.FilterCandidates import FilterCandidatesByWrongLetters
from Functions.Filters.FilterCandidatesByCorrectPositions import FilterCandidatesByCorrectPositions
from Functions.Filters.FilterCandidatesByWrongPositions import FilterCandidatesByWrongPositions
from Functions.Filters.FilterCandidatesByAbscense import FilterCandidatesByAbscense
from Functions.Entropy.CalcEntropies import CalcEntropies
from Infra.FetchInitialWord import FetchInitialWord
from Infra.FetchAllWords import FetchAllWords

def main():

    word = FetchInitialWord()
    candidates = FetchAllWords()
    guesses = {}
    viewGuesses = {}
    allWrongLetters = []
    guessedWords = []

    for i in range(5):
        
        guess = input("Insira sua tentativa [5 letras]: ")
        guessedWords.append(guess)
        viewTemplate, guessTemplate, wrongLetters = VerifyAnswer(guess, word)

        guesses[i] = guessTemplate
        viewGuesses[i] = viewTemplate

        allWrongLetters.extend(x for x in wrongLetters if x not in allWrongLetters)

        for i in range(len(viewGuesses)):
            print(*viewGuesses[i])

        correctPositions, wrongPositions = GetPositions(guesses, guessedWords)

        #Filters 
        candidates = FilterCandidatesByWrongLetters(candidates, allWrongLetters)
        candidates = FilterCandidatesByCorrectPositions(correctPositions, candidates)
        candidates = FilterCandidatesByWrongPositions(wrongPositions, candidates)
        candidates = FilterCandidatesByAbscense(wrongPositions, candidates)
        
        if(i >= 1):
            entropies = CalcEntropies(candidates)
            bestWord = max(entropies, key=entropies.get)

            print("Palavra sugerida:", bestWord)
        
    print("Palavra correta: ", word)

    return 0

if __name__ == "__main__":
    main()