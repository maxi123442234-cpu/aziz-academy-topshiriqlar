n = int(input())
s = list(map(int, input().split()))
y = 0
for x in s:
    if x % 2 == 0:
    	y += x
print(y)