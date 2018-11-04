def EightQueens(a):
    n = []
    for i in a:
        n.append([int(i[1]), int(i[3])])
    for i in range(len(n) - 1):
        for l in range(i + 1, len(n)):
            ax, ay, bx, by = n[i][0], n[i][1], n[l][0], n[l][1]
            if ax == bx or ay == by or ax - bx == ay - by:
                return '(' + str(ax) + ',' + str(ay) + ')'
    return 'true'


print (EightQueens(raw_input()))