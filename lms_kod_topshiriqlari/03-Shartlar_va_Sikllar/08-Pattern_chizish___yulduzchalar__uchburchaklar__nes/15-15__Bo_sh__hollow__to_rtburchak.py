n, m = map(int, input().split())
for i in range(n):
    q = ""
    for j in range(m):
        
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            q += "*"
        else:
            q += '.'
    print(q)