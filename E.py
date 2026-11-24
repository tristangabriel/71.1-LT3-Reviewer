def la():
    n, k = [int(_) for _ in input().split()]
    x = [int(_) for _ in input().split()]
    histo = {}
    for y in x:
        if y in histo:
            histo[y]+=1
        else:
            histo[y]=1
    cnt = 0
    for y in histo.keys():
        cnt += histo[y]-1
        for a in range(1, k+1):
            if (a+y) in histo:
                print(y, a+y)
                cnt += histo[a+y]*histo[y]
    print(cnt)