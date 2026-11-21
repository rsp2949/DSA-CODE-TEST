n = int(input())
arr = list(map(int, input().split()))
cnt = [0] * 101
for x in arr:
    cnt[x] += 1
out = []
for v in range(101):
    for _ in range(cnt[v]):
        out.append(str(v))
print(" ".join(out))
