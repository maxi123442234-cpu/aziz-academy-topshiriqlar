n = int(input())
s = list(map(int, input().split()))
m = 0
for son in s:
    if son > 0:
        m += 1
        
print(m)