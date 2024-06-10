def make_rug(m, n, s):
    rugs = []
    if s == "" or s is None:
        s = "#"
    for i in range(0, m):
        rugs.append(s * n)
    return rugs


print(make_rug(3, 5, '#'))
print(make_rug(3, 5, '$'))
print(make_rug(2, 2, 'A'))
print(make_rug(7, 9, 'R'))
