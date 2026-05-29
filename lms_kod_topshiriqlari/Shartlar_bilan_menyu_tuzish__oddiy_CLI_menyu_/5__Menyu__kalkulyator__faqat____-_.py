a, b, c = map(str, input().split())
if c == "+":
    print(int(a) + int(b))
elif c == "-":
    print(int(a) - int(b))
else:
    print("Invalid")