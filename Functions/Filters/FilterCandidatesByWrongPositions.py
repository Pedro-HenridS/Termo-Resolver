from collections import Counter

def FilterCandidatesByWrongPositions(wrongPositionsCollections: dict, words: list, wrongLetters: list, lettersCount):

    filtered = []
    filtered2 = [] #pra palavras erradas, pra nao usar diretamente o Filtered

    for word in words:
        valid = True

        for position, letter in wrongPositionsCollections.items():
            if word[position] == letter:
                valid = False
                break

        if valid:
            filtered.append(word)

    #esse for pra achar as palavras com menos letras ou mais letras que o minimo e o maximo.
    for word in words:
        
        tempWordLetters = Counter(word)

        #isso aqui eu pecorro só os char da palavra
        for char in word:

            #Basicamente: Se uma palavra tiver uma letra que aparece menos que x vezes do que o contador, ela tem menos que o minino, x é o minimo, ou seja, errada.
            if (tempWordLetters[char] < lettersCount[char]):
                filtered2.append(word)
                break

            #Basicamente 2: Se o contador tiver uma letra com repetições x vezes, com x > 0, E, eu disse E <- (enfasis), essa mesma letra esta em WrongLetters, siginifica que x é a quantidade máxima que a palavra correta tem daquela letra.
            #Basicamente 3: Se o contador tiver uma letra com repetições x vezes, com x > 0, MAAAAAS se a letra NAO estiver em wrongLetters, sigifnica que ainda nao da pra saber a quantidade maxima.
            if (char in wrongLetters) and (tempWordLetters[char] > lettersCount[char]):
                filtered2.append(word)
                break
        
        #isso aqui eu pecorro só os char do letterCount.
        for char, count in lettersCount.items():
            if tempWordLetters[char] < count:
                if word not in filtered2:
                    filtered2.append(word)
                    break
     
    filtered = (set(filtered) - set(filtered2))
    return filtered