n = int(input())
s = list(map(int, input().split()))
y = 0 
for son in s:
    y += son
    print(y)