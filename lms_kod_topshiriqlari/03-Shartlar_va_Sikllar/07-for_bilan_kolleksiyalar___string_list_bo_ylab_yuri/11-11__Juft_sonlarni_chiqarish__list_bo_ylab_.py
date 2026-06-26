n = int(input())

s = input().split()
for i in range(n):
    a = int(s[i])
    if a % 2 == 0:
        print(a)