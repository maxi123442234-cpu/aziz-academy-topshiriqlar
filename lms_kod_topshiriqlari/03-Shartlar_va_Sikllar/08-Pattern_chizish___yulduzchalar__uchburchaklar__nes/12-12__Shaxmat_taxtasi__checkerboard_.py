n, m = map(int, input().split())

for i in range(n):
    q = ""
    for j in range(m):
        if (i + j) % 2 == 0:
            q += '*'
        else:
            q += "."
    print(q)