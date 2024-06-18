def tallest_skyscraper(skyline):
    for i in range(0, len(skyline)):
        for j in range(0, len(skyline[i])):
            if skyline[i][j] == 1:
                return len(skyline) - i


print(tallest_skyscraper([[0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 0],
                          [0, 0, 1, 0, 1, 0],
                          [0, 1, 1, 1, 1, 0],
                          [1, 1, 1, 1, 1, 1]]))
print(tallest_skyscraper([
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 1]
]))

print(tallest_skyscraper([
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 1]
]))

print(tallest_skyscraper([
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 1, 1, 0],
    [1, 1, 1, 1]
]))
