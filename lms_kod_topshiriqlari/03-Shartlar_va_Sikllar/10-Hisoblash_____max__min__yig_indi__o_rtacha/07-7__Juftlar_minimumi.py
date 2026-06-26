n = int(input())
n = list(map(int, input().split()))
a = []
for x in n:
    if x % 2 == 0:
        a .append(x)
if len(a) == 0:
    print("No")
else:
    print(min(a))