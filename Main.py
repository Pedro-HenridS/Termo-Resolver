from Functions.VerifyAnswer import VerifyAnswer

def main():

    attempt = input("Insira sua tentativa [5 letras]: ")
    
    template, wrongLetters = VerifyAnswer(attempt, "praia")

    print(template)
    print(wrongLetters)

    return 0

if __name__ == "__main__":
    main()