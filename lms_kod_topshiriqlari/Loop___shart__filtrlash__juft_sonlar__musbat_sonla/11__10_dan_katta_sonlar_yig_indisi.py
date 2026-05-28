n = int(input())
s = list(map(float, input().split()))

y = 0 

for son in s:
    if son > 10:
        y += son 
print(int(y) if y.is_integer() else y)