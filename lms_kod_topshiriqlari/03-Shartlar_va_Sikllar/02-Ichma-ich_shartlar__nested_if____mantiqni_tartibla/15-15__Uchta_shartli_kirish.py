r, a = map(str, input().split())
if r == "admin":
    if a == 1:
        print("Admin inactive")
    else:
        print("Admin active")
else:
    print("User")
