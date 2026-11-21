n, k = map(int, input().split())
arr = list(map(int, input().split()))
win = 0
for i in range(k):
    win += arr[i]
best = win
for i in range(k, n):
    win += arr[i] - arr[i - k]
    if win > best:
        best = win
print(best)
