a = input()
b = input()

s = a.strip().capitalize() == "True"
d = b.strip().capitalize() == "True"

n = s or d 
print(n)