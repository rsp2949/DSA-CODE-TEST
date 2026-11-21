import sys
data = sys.stdin.read().split()
n, q = int(data[0]), int(data[1])
pref = [0] * (n + 1)
for i in range(n):
    pref[i + 1] = pref[i] + int(data[2 + i])
idx = 2 + n
out = []
for _ in range(q):
    l, r = int(data[idx]), int(data[idx + 1])
    idx += 2
    out.append(str(pref[r + 1] - pref[l]))
print("\n".join(out))
