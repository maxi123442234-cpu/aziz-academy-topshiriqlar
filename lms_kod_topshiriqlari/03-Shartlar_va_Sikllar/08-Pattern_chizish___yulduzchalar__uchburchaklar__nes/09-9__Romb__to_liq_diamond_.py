n = int(input())

for i in range(1, n + 1):
    p = ' ' * (n - i)
    y = '*' * (2 * i - 1)
    print(p + y)
for i in range(n - 1, 0, -1):
    p = ' ' * (n - i)
    y = "*" * (2 * i -1)
    print(p + y)