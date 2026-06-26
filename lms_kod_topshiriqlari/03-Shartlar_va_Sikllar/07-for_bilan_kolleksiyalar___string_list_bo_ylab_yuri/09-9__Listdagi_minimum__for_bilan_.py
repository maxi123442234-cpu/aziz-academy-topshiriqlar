n = int(input())

s = input().split()
m = int(s[0])
for i in range(n):
    j = int(s[i])
    if j < m:
        m = j 
print(m)