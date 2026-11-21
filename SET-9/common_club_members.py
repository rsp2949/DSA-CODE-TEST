m, n = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
setA = set(A)
common_set = set()
for x in B:
    if x in setA:
        common_set.add(x)
common = list(common_set)
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
ans = msort(common)
print(" ".join(map(str, ans)) if ans else "None")
