w = input().split()
m = w[0]
for word in w:
    if len(word) > len(m):
        m = word
print(m)