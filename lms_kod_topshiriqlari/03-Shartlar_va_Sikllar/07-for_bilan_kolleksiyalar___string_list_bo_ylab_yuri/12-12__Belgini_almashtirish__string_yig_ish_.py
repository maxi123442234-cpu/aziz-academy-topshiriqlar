s = input()
y = ""
for belgi in s:
    if belgi == "a":
        y += "@"
    else:
        y += belgi
print(y)