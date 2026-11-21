n = int(input())
arr = list(map(int, input().split()))
last = {}
l = best = 0
for r in range(n):
    x = arr[r]
    if x in last and last[x] >= l:
        l = last[x] + 1
    last[x] = r
    if r - l + 1 > best:
        best = r - l + 1
print(best)
