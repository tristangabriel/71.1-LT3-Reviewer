n, B = [int(_) for _ in input().split()]
p = [int(_) for _ in input().split()]
print(sum(a+b+c+d==B for a in p for b in p for c in p for d in p))