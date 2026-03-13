from Functions.VerifyAnswer import VerifyAnswer
from Functions.FilterCandidates import FilterCandidatesByWrongLetters
from Infra.FetchInitialWord import FetchInitialWord
from Infra.FetchAllWords import FetchAllWords

def main():

    word = FetchInitialWord()
    candidates = FetchAllWords()
    guesses = {}
    viwwGuesses = {}
    allWrongLetters = []

    for i in range(5):
    
        guess = input("Insira sua tentativa [5 letras]: ")
        viewTemplate, template, wrongLetters = VerifyAnswer(guess, word)

        guesses[i] = template
        viwwGuesses[i] = viewTemplate

        # Adiciona as letras erradas da analise atual a lista completa de letras erradas 
        allWrongLetters.extend(x for x in wrongLetters if x not in allWrongLetters)

        for i in range(len(viwwGuesses)):
            print(*viwwGuesses[i])

        candidates = FilterCandidatesByWrongLetters(candidates, allWrongLetters)

        # for word in candidates:
        #     print(word)    

    
        
    for i, letter in enumerate(allWrongLetters):
            print(letter, end=" ")

    print("Palavra correta: ", word)

    return 0

if __name__ == "__main__":
    main()