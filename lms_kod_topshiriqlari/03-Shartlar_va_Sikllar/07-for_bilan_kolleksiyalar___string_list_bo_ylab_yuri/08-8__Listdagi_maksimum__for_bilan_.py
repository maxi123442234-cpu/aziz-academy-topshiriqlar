n = int(input())
s = list(map(int, input().split()))
e = s[0]

for i in range(1, n):
    if s[i]	> e:
        e = s[i]
print(e)