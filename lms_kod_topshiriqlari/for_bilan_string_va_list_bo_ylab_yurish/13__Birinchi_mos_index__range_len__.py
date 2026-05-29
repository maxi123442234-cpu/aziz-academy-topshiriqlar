n = int(input())
lst = input().split()
x = input()
a = -1 
for i in range(len(lst)):
    if lst[i] == x:
        a = i 
        break
print(a)