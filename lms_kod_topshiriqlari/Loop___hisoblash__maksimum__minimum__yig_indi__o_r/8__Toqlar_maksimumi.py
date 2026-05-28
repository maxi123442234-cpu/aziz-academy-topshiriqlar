n = int(input())
n = list(map(int, input(). split()))
t = []
for x in n:
    if x % 2 != 0:
        t.append(x)
if len(t) == 0:
    print("No")
else:
    print(max(t))