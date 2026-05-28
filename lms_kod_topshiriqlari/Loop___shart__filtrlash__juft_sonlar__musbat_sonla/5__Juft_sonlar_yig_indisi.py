n = int(input())
s = list(map(int, input().split()))
print(sum(x for x in s if x % 2 == 0))