n = int(input())
for i in range(n):
    q = ""
    for j in range(n):
        if i == j or i + j == n - 1:
            q += '*'
        else:
            q += '.'
    print(q)