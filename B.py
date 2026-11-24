d = {}
li = {}
n = int(input())
for i in range(n):
    name, op, g = input().split()
    if op=="GRADE":
        d[name] = g
    else:
        li[name] = g
for name, subm in li.items():
    if subm in d:
        li[name]=d[subm]
    else:
        li[name]=0
names=sorted(list(d.keys()) + list(li.keys()))
for name in names:
    print(name, d[name] if name in d else li[name])