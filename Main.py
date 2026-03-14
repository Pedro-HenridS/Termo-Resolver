from Functions.VerifyAnswer import VerifyAnswer
from Functions.GetPositions import GetPositions
from Functions.FilterCandidates import FilterCandidatesByWrongLetters
from Functions.FilterCandidatesByCorrectPositions import FilterCandidatesByCorrectPositions
from Functions.FilterCandidatesByWrongPositions import FilterCandidatesByWrongPositions
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

        candidates = FilterCandidatesByWrongLetters(candidates, allWrongLetters)
   
        correctPositions, wrongPositions = GetPositions(guesses, guessedWords)
        candidates = FilterCandidatesByCorrectPositions(correctPositions, candidates)
        candidates = FilterCandidatesByWrongPositions(wrongPositions, candidates)
        
        for candidate in candidates:
             print(candidate)
        
    for i, letter in enumerate(allWrongLetters):
            print(letter, end=" ")

    print("Palavra correta: ", word)

    return 0

if __name__ == "__main__":
    main()