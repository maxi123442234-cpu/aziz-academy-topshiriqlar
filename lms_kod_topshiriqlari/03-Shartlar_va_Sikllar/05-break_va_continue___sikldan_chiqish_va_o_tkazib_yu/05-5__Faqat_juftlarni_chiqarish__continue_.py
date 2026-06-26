n = int(input())
i = 1
while i in range(1, n + 1):
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1