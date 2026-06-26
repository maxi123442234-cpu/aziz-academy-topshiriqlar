n = int(input())
a = list(map(int, input().split()))
b = sum(a) / n
c = 0
for x in a:
    if x > b:
        c += 1
print(c)