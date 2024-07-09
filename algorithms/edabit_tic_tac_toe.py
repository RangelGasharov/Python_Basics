def tic_tac_toe(mtrx):
    for i in range(0, len(mtrx)):
        if mtrx[i][0] == mtrx[i][1] == mtrx[i][2]:
            if mtrx[i][0] == "X":
                return "Player 1 wins"
            elif mtrx[i][0] == "O":
                return "Player 2 wins"
    for i in range(0, len(mtrx[0])):
        if mtrx[0][i] == mtrx[1][i] == mtrx[2][i]:
            if mtrx[0][i] == "X":
                return "Player 1 wins"
            elif mtrx[0][i] == "O":
                return "Player 2 wins"
    if mtrx[0][0] == mtrx[1][1] == mtrx[2][2]:
        if mtrx[1][1] == "X":
            return "Player 1 wins"
        elif mtrx[1][1] == "O":
            return "Player 2 wins"
    if mtrx[2][0] == mtrx[1][1] == mtrx[0][2]:
        if mtrx[1][1] == "X":
            return "Player 1 wins"
        elif mtrx[1][1] == "O":
            return "Player 2 wins"
    return "It's a Tie"


print(tic_tac_toe([["X", "O", "O"], ["O", "X", "O"], ["O", "#", "X"]]))
print(tic_tac_toe([["X", "O", "O"], ["O", "X", "O"], ["X", "#", "O"]]))
print(tic_tac_toe([["X", "X", "O"], ["O", "X", "O"], ["X", "O", "#"]]))
