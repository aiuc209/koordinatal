def masofa(royxat):
    natijalar = []
    for nuqta in royxat:
        x, y = nuqta
        masofa_x = abs(x)
        masofa_y = abs(y)
        natijalar.append(min(masofa_x, masofa_y))
    return natijalar

royxat = [(1, 2), (3, 4), (5, 6)]
print(masofa(royxat))
