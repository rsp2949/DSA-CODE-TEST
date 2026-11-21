n, T = map(int, input().split())
arr = list(map(int, input().split()))
best = cur = 0
for x in arr:
    if x >= T:
        cur += 1
        if cur > best:
            best = cur
    else:
        cur = 0
print(best)
