a = (input())
b = (input())

s = a.strip().capitalize() == "True"
g = b.strip().capitalize() == "True"

n = s and g 
print(n)