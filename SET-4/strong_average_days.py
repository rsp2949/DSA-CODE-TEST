n, k, T = map(int, input().split())
arr = list(map(int, input().split()))
target = k * T
win = 0
for i in range(k):
    win += arr[i]
cnt = 1 if win >= target else 0
for i in range(k, n):
    win += arr[i] - arr[i - k]
    if win >= target:
        cnt += 1
print(cnt)
