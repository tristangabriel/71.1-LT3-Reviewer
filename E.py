kiss = {}
for _ in range(3):
    row = input()
    for i in range(len(row)):
        kiss[row[i]] = (_, i)

cnt, x, y = 1, 0, 0
for c in input():
    cnt += abs(kiss[c][0]-x) + abs(kiss[c][1]-y) + 1
    x, y = kiss[c]

print(cnt)