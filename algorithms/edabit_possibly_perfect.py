def possibly_perfect(solutions, given_answers):
    if len(solutions) != len(given_answers):
        return False
    for i in range(len(solutions)):
        if solutions[i] != given_answers[i] and solutions[i] != "_":
            return False
    return True


print(possibly_perfect(['A', '_', 'C', '_', 'B'], ['A', 'D', 'C', 'E', 'B']))
print(possibly_perfect(['B', '_', 'B'], ['B', 'D', 'C']))
print(possibly_perfect(['T', '_', 'F', 'F', 'F'], ['F', 'F', 'T', 'T', 'T']))
print(possibly_perfect(['B', 'A', '_', '_'], ['B', 'A', 'C', 'C']))
print(possibly_perfect(['A', 'B', 'A', '_'], ['B', 'A', 'C', 'C']))
print(possibly_perfect(['_', 'T', 'T', 'T'], ['T', 'T', 'F', 'T']))
print(possibly_perfect(['_', 'T', 'T', 'T'], ['T', 'T', 'T', 'T']))
