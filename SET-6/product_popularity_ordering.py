n = int(input())
arr = list(map(int, input().split()))
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1
items = [(freq[x], -x, x) for x in freq]
def msort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    L, R = msort(a[:mid]), msort(a[mid:])
    res = []
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            res.append(L[i]); i += 1
        else:
            res.append(R[j]); j += 1
    while i < len(L):
        res.append(L[i]); i += 1
    while j < len(R):
        res.append(R[j]); j += 1
    return res
out = []
for f, _, pid in msort(items):
    s = str(pid)
    for _ in range(f):
        out.append(s)
print(" ".join(out))
