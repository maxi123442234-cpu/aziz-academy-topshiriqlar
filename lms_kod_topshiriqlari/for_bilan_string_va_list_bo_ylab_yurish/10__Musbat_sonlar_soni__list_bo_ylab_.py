n = int(input())
s = input().split()
m = 0 
for i in range(n):
    a = int(s[i])
    if a > 0:
        m += 1 
print(m)