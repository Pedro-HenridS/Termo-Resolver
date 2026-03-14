import math
from collections import defaultdict
from Functions.Entropy.CalcPattern import CalcPattern

def CalcEntropies(candidates: list[str]):
    entropies = {}

    for guess in candidates:
        patternCounter = defaultdict(int)

        for target in candidates:
            pattern = CalcPattern(guess, target)
            patternCounter[pattern] += 1

        total = len(candidates)
        entropy = 0.0

        for count in patternCounter.values():
            p = count / total
            entropy -= p * math.log2(p)

        entropies[guess] = entropy

    return entropies