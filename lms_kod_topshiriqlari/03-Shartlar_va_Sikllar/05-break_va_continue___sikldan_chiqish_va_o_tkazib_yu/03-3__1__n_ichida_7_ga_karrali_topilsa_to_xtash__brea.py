n = int(input())

i = 1 
t = False

while i <= n:
    if i %7 == 0:
        print(i)
        t = True
        break
    i += 1 
    
if not t:
    print("No")