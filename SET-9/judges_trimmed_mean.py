n, t = map(int, input().split())
arr = list(map(int, input().split()))
cnt = [0] * 101
for x in arr:
    cnt[x] += 1
sorted_arr = []
for v in range(101):
    for _ in range(cnt[v]):
        sorted_arr.append(v)
total = 0
for i in range(t, n - t):
    total += sorted_arr[i]
print("%.2f" % (total / (n - 2 * t)))
