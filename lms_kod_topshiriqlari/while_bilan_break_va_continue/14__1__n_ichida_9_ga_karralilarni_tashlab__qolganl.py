n = int(input())
i = 1
y = 0
while i <= n:
    if i % 9 == 0:
        i += 1 
        continue
    y += i 
    i += 1
print(y)