from collections import Counter

#lista teste, vamo usar api dps
wordList = [
    "carta",
    "piano",
    "verde",
    "livro",
    "nuvem",
    "canto",
    "prato",
    "lente",
    "pedra",
    "campo",
    "festa",
    "corte",
    "poder",
    "viver",
    "luzir",
    "brisa",
    "folha",
    "areia",
    "caixa",
    "pauta",
    "sonho",
    "claro",
    "pular",
    "beijo",
    "magia",
    "tempo",
    "risco",
    "linha",
    "pilar",
    "vento"
]

dayWord = "pedra"

#teoricamente funcionando, preciso testar mais dps
def verifiryAnsewer(word, dayWord):
    
    dayWordLetters = Counter(dayWord)

    #0 = errado demais slc, 1 = correto, 2 = meio correto
    correctSpace = [0,0,0,0,0]

    #aqui é pra verificcar se a letra ta na posição correta
    for x in range(5):
        if word[x] == dayWord[x]:
            correctSpace[x] = 1
            dayWordLetters = dayWordLetters - Counter(dayWord[x])
    
    #aqui é pra ver se a letra ta na palavra, mas nao ta na posicao certa.
    #Sim Pedro, precisa de 2 for diferente kkkkk
    for x in range(5):
        if word[x] in dayWordLetters:
            correctSpace[x] = 2
            dayWordLetters = dayWordLetters - Counter(word[x])

    print(correctSpace) #printei pra testar, mas nao precisa disso, lembrete: apagar isso dps.
    return correctSpace



#Falta implementar a remoção no caso de "0" e testar dps
def removeWord(wordList, correctLetters, previusWord):
    '''Remover palavras da lista com base nas letras certas, meio certas, e erradas ta. 
 correctLetters é uma lista, Pedro.
 Retorna a lista só com as palavras possiveis'''
    
    newWordList = list(wordList)
    for word in wordList:
        tempWordLetters = Counter(word) #é dificil de explicar o pq disso escrevendo aqui, qualquer coisa de te explico dps
        invalid = False  #fiz isso aqui pra conseguir dar um "Break" e poder pular pra proxima palavra

        #Se prepara pra ver 3 for seguido, uma aberração
        for x in range(5):
            # esse for aqui vai remover as palavras da lista que nao tem as letras certas no lugar certo
            if (correctLetters[x] == 1): 
                if (word[x] != previusWord[x]):
                    newWordList.remove(word)
                    invalid = True
                    break
                else:
                    tempWordLetters = tempWordLetters - Counter(word[x])
        if invalid:
            continue

        for y in range(5):
            #ja esse for é pra remover palavras que nao tenha a letra que ta na posicao errada
            #nao adianta reclamar Pedro, vai ser 3 for sim, ponto final.
            if(correctLetters[y] == 2):
                if (previusWord[y]  not in tempWordLetters) or (word[y] == previusWord[y]):
                    newWordList.remove(word)
                    invalid = True
                    break

                else:
                    tempWordLetters = tempWordLetters - Counter(previusWord[y])
        if invalid:
            continue

        # esse aqui vai ser pra remover todas as palavras que tem letras que nao estao na palavra certa
        # Luiz do futuro, lembre de implementar isso depois, seu safado preguisoço.
        
        for z in range(5):
            return 0
        
        return newWordList
    



# A fazer/pensar/nao confirmado
def wordSimilirity():
    return 0

def wordChoise():
    return 0




            
        


