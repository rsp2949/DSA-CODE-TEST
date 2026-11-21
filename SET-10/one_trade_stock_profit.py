n = int(input())
arr = list(map(int, input().split()))
min_p = arr[0]
best = 0
for i in range(1, n):
    diff = arr[i] - min_p
    if diff > best:
        best = diff
    if arr[i] < min_p:
        min_p = arr[i]
print(best)
