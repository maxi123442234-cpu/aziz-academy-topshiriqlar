n = int(input())
m = n // 2 
for i in range(n):
    q = ""
    for j in range(n):
        if i == m or j == m:
            q += "*"
        else:
            q += '.'
    print(q)