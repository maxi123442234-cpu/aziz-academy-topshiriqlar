n = int(input())
n = list(map(int, input().split()))
s = 0 
for x in n:
    if x > 0:
        s += x
print(s)