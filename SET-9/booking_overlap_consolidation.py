import sys
data = sys.stdin.read().split()
n = int(data[0])
ivs = [[int(data[1 + 2 * i]), int(data[2 + 2 * i])] for i in range(n)]
def msort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    L, R = msort(a[:mid]), msort(a[mid:])
    res = []
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i][0] < R[j][0] or (L[i][0] == R[j][0] and L[i][1] <= R[j][1]):
            res.append(L[i]); i += 1
        else:
            res.append(R[j]); j += 1
    while i < len(L):
        res.append(L[i]); i += 1
    while j < len(R):
        res.append(R[j]); j += 1
    return res
ivs = msort(ivs)
merged = [ivs[0]]
for i in range(1, n):
    if ivs[i][0] <= merged[-1][1]:
        if ivs[i][1] > merged[-1][1]:
            merged[-1][1] = ivs[i][1]
    else:
        merged.append(ivs[i])
print("\n".join(f"{a} {b}" for a, b in merged))
