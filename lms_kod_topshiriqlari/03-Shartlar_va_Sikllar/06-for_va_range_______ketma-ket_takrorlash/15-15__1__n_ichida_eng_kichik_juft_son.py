n = int(input())
m = None
for i in range(1, n + 1):
    if i % 2 == 0:
        m = i 
        break
if m is not None:
    print(m)
else:
    print("No")