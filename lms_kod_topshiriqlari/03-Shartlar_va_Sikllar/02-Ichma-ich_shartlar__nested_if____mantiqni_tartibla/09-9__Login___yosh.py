u, a = map(str, input().split())
if u == "admin":
    if int(a) >= 18:
        print("Full access")
    else:
        print("Limited")
else:
    print("No access")
