tree={}
n = int(input())
for _ in range(n):
    pa, op, op, op, op, name = input()[:-1].split()
    if pa in tree:
        tree[pa].append(name)
    else:
        tree[pa] = [name]
    if name not in tree:
        tree[name] = []
gp=input()
if gp not in tree:
    print("NOT A RELATIVE")
else:
    li = []
    for child in tree[gp]:
        if child in tree:
            li.extend(tree[child])
    li.sort()
    if len(li):
        print(*li)
    else:
        print("NO GRANDCHILDREN")