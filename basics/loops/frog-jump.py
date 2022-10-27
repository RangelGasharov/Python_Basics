frogJumpLength = 1.0
STREET_WIDTH = float(input("Write down the width of the street.\n"))
TOTAL_JUMPS = int(input("Please write down the total amount of jumps\n"))
coveredDistance = 0

for i in range(1, TOTAL_JUMPS):
    print(f"{i}.:", frogJumpLength)
    coveredDistance += frogJumpLength
    frogJumpLength /= 2
if coveredDistance >= STREET_WIDTH:
    print("Goal has been reached!")
else:
    print("Goal has not been reached!")
print(f"Covered distance after {TOTAL_JUMPS} jumps:", coveredDistance)
