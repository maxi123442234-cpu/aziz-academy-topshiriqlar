n = int(input())
i = 1 
j = 0
t = False
while i <= n:
    if i % 2 == 0:
        j += 1
    if j == 3:
        print(i)
        t = True
        break
    i += 1
    
if not t:
    print("No")