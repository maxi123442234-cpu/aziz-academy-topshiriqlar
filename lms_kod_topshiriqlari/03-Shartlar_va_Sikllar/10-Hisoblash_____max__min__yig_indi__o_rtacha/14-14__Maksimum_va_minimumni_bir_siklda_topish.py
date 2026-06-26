n = int(input())
s = list(map(int, input().split()))
mx = s[0]
mn = s[0]
for son in s:
    if son > mx:
        mx = son
    if son < mn:
        mn = son
print(mx, mn)