y = 0
s = 0 	

while True:
    a = int(input())
    
    if a == 0:
        break
        
    y += a
    s += 1
if s == 0:
    print(0)
else:
    o = y / s
    print(o)