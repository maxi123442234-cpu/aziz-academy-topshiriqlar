s = input()
r = "0123456789"
c = 0 
for b in s:
    if b in r:
        c += 1
print(c)