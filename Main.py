import random
from Functions.VerifyAnswer import VerifyAnswer
from Functions.GetPositions import GetPositions
from Functions.Filters.FilterCandidates import FilterCandidatesByWrongLetters
from Functions.Filters.FilterCandidatesByCorrectPositions import FilterCandidatesByCorrectPositions
from Functions.Filters.FilterCandidatesByWrongPositions import FilterCandidatesByWrongPositions
from Functions.Filters.FilterCandidatesByAbscense import FilterCandidatesByAbscense
from Functions.Entropy.CalcEntropies import CalcEntropies
from Infra.FetchInitialWord import FetchInitialWord
from Infra.FetchAllWords import FetchAllWords


MAX_ATTEMPTS = 6
VALID_FEEDBACK = {1, 0, -1}


def load_words():
    return sorted({word.strip().lower() for word in FetchAllWords() if len(word.strip()) == 5})


def format_feedback(guess, pattern):
    rendered = []

    for letter, status in zip(guess, pattern):
        if status == 1:
            rendered.append("✅ " + letter)
        elif status == -1:
            rendered.append("🟨 " + letter)
        else:
            rendered.append("🟥 " + letter)

    return rendered


def filter_candidates(candidates, guess, pattern):
    return [candidate for candidate in candidates if CalcPattern(guess, candidate) == pattern]


def get_best_word(candidates):
    if not candidates:
        return None

    entropies = CalcEntropies(candidates)
    best_word = max(entropies, key=entropies.get)
    return best_word, entropies[best_word]


def parse_feedback(raw_feedback):
    normalized = raw_feedback.replace(",", " ").split()

    if len(normalized) != 5:
        return None

    try:
        pattern = tuple(int(value) for value in normalized)
    except ValueError:
        return None

    if any(value not in VALID_FEEDBACK for value in pattern):
        return None

    return pattern


def prompt_guess(allowed_words=None):
    while True:
        guess = input("Insira uma palavra [5 letras]: ").strip().lower()

        if len(guess) != 5 or not guess.isalpha():
            print("Entrada invalida. Digite uma palavra com 5 letras.")
            continue

        if allowed_words is not None and guess not in allowed_words:
            print("Palavra nao encontrada na base.")
            continue

        return guess


def choose_mode():
    print("Escolha o modo:")
    print("1 - Jogar Termo no terminal")
    print("2 - Assistente para Termo no navegador")

    while True:
        mode = input("Modo: ").strip()
        if mode in {"1", "2"}:
            return mode

        print("Modo invalido. Escolha 1 ou 2.")


def run_terminal_game(all_words):
    secret_word = random.choice(all_words)
    candidates = list(all_words)
    history = []

    for attempt in range(1, MAX_ATTEMPTS + 1):
        guess = prompt_guess(all_words)
        pattern = CalcPattern(guess, secret_word)
        history.append(format_feedback(guess, pattern))

        if guess in candidates and guess != secret_word:
            candidates.remove(guess)

        candidates = filter_candidates(candidates, guess, pattern)

        for row in history:
            print(*row)

        if pattern == (1, 1, 1, 1, 1):
            print(f"Voce acertou em {attempt} tentativa(s).")
            return 0

        print(f"Palavras possiveis: {len(candidates)}")

        if attempt >= 2 and candidates:
            best_word, entropy = get_best_word(candidates)
            print(f"Palavra sugerida: {best_word} (entropia: {entropy:.4f})")

    print("Palavra correta:", secret_word)
    return 0


def run_browser_assistant(all_words):
    candidates = list(all_words)
    mode = int(input("Com quantas palavras voce esta jogando? ").strip())

    print("Informe a palavra tentada e o resultado de cada posicao.")
    print("Use 1 para certo, -1 para letra na palavra em posicao errada, e 0 para letra ausente.")
    print("Exemplo de resultado: 1 -1 0 0 1")
    print("Pressione Enter sem digitar palavra para sair.")

    number_of_words(mode, candidates)


    ''' while True:
        guess = input("Palavra tentada: ").strip().lower()

        if not guess:
            return 0

        if len(guess) != 5 or not guess.isalpha():
            print("Entrada invalida. Digite uma palavra com 5 letras.")
            continue

        feedback = parse_feedback(input("Resultado [5 valores]: ").strip())
        if feedback is None:
            print("Resultado invalido. Use exatamente 5 valores entre 1, 0 e -1.")
            continue

        candidates = filter_candidates(candidates, guess, feedback)

        print(f"Palavras possiveis: {len(candidates)}")
        if candidates:
            print("Algumas opcoes:", ", ".join(candidates[:10]))
            print("Melhor proxima palavra:", get_best_word(candidates))
        else:
            print("Nenhuma palavra encontrada. Verifique se a tentativa e o resultado foram informados corretamente.")
'''
def number_of_words(quantidade_palavras, candidates):
    Max_Attempts= MAX_ATTEMPTS + int(quantidade_palavras) - 1
    word_Lists = {}
    invalid = False
    

    for attempts in range(Max_Attempts):
        word_Entropies = {}
        temp_word_Lists = []
        while True:
                guess = input(str(attempts + 1) + " - Palavra tentada: ").strip().lower()

                if not guess:
                    return 0

                if len(guess) != 5 or not guess.isalpha():
                    print("Entrada invalida. Digite uma palavra com 5 letras.")
                    continue
                break
                
        for words in range(quantidade_palavras):
            temp_Canditades = []
            while True:
                feedback = parse_feedback(input("Resultado da palavra " + str(words + 1) + "[5 valores]: ").strip())
                if feedback is None:
                    print("Resultado invalido. Use exatamente 5 valores entre 1, 0 e -1.")
                    continue
                break
            if feedback == (1, 1, 1, 1, 1):
                print(f"Palavra {words + 1} acertada em {attempts + 1} tentativa(s).")
                continue
            base_candidates = candidates if attempts == 0 else word_Lists[words]
            filtered_candidates = filter_candidates(base_candidates, guess, feedback)
            print(f"Guess: {guess}")
            print(f"Feedback informado para a palavra {words + 1}: {feedback}")
            print(f"Candidatos antes do filtro para a palavra {words + 1}: {base_candidates}")
            print(f"Palavra {words + 1}: {len(base_candidates)} -> {len(filtered_candidates)} candidatos")
            print(f"Candidatos depois do filtro para a palavra {words + 1}: {filtered_candidates}")

            if not filtered_candidates:
                print(f"Nenhuma candidata restante para a palavra {words + 1}.")
                print("Isso indica feedback inconsistente, palavra ausente no dicionario ou divergencia na regra de avaliacao.")
                print("Alguns candidatos antes do filtro e seus padroes calculados:")
                for candidate in base_candidates[:10]:
                    print(f"  {candidate}: {CalcPattern(guess, candidate)}")
                return 1

            word_Lists[words] = filtered_candidates

            best = get_best_word(word_Lists[words])
            if best is not None:
                best_word, best_word_entropy = best
                word_Entropies[best_word] = best_word_entropy
                print(f"Melhor palavra para a lista da palavra {words + 1}: {best_word} (entropia: {best_word_entropy:.4f})")
         
        for keys in word_Lists:
            if len(word_Lists[keys]) == 1:
                print(f"Palavra sugerida: {word_Lists[keys][0]}")
                invalid = True
                break
            for elem in word_Lists[keys]:
                if elem not in temp_word_Lists:
                    temp_word_Lists.append(elem)
        if invalid:
            continue
        
        print(f"Uniao de candidatos considerada no turno: {temp_word_Lists}")
        
                 
        best = get_best_word(temp_word_Lists)
        if best is not None:
            best_word, best_word_entropy = best
            word_Entropies[best_word] = best_word_entropy
            print(f"Melhor palavra para a uniao das listas: {best_word} (entropia: {best_word_entropy:.4f})")

        print(f"word_Entropies no turno {attempts + 1}: {word_Entropies}")

        if word_Entropies:
            best_suggestion = max(word_Entropies, key=word_Entropies.get)
            print(f"Palavra sugerida: {best_suggestion} (entropia: {word_Entropies[best_suggestion]:.4f})")
        

def main():
    all_words = load_words()
    mode = choose_mode()

    if mode == "1":
        return run_terminal_game(all_words)

    return run_browser_assistant(all_words)


if __name__ == "__main__":
    main()