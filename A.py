def finding(r, c, grid):
    d = {'R': [], 'B': []}
    for i in range(r):
        for j in range(c):
            if grid[i][j]!='.':
                d[grid[i][j]].append((i, j))
    return d

def cover(p1, p2, letter):
    global grid
    valid = letter+'.'
    if p1[0]==p2[0]:
        for m in range(p1[1], p2[1]+1):
            grid[p1[0]][m]= letter if (grid[p1[0]][m] in valid) else 'P'
    else:
        for m in range(p1[0], p2[0]+1):
            grid[m][p1[1]]= letter if (grid[m][p1[1]] in valid) else 'P'


    

r, c = [int(_) for _ in input().split()]
grid = [list(input()) for _ in range(r)]
d = finding(r, c, grid)
cover(d['R'][0], d['R'][1], 'R')
if len(d['B']):
    cover(d['B'][0], d['B'][1], 'B')

for row in grid:
    print(''.join(row))
