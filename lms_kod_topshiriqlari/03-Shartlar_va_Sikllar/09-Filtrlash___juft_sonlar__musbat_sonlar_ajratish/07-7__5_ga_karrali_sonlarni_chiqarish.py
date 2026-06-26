n = int(input())
s = list(map(int, input().split()))
[print(x) for x in s if x % 5 == 0]