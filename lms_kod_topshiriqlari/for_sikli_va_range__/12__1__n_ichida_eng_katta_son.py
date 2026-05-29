n = int(input())
m = 0
for i in range(1, n + 1):
    if i > m:
        m = i
print(m)