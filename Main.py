import random

from Functions.Entropy.CalcEntropies import CalcEntropies
from Functions.Entropy.CalcPattern import CalcPattern
from Infra.FetchAllWords import FetchAllWords


MAX_ATTEMPTS = 10
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
    return max(entropies, key=entropies.get)


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
            print("Palavra sugerida:", get_best_word(candidates))

    print("Palavra correta:", secret_word)
    return 0


def run_browser_assistant(all_words):
    candidates = list(all_words)

    print("Informe a palavra tentada e o resultado de cada posicao.")
    print("Use 1 para certo, -1 para letra na palavra em posicao errada, e 0 para letra ausente.")
    print("Exemplo de resultado: 1 -1 0 0 1")
    print("Pressione Enter sem digitar palavra para sair.")

    while True:
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


def main():
    all_words = load_words()
    mode = choose_mode()

    if mode == "1":
        return run_terminal_game(all_words)

    return run_browser_assistant(all_words)


if __name__ == "__main__":
    main()
