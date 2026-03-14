def FilterCandidatesByAbscense(wrongPositionsCollections: dict, candidates: list):

    processedCandidates = []

    for letter in wrongPositionsCollections.values():
        for candidate in candidates:
            if letter in candidate:
                processedCandidates.append(candidate)

    return processedCandidates 
    