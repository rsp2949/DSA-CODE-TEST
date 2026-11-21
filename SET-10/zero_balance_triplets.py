n = int(input())
arr = list(map(int, input().split()))
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
arr = msort(arr)
out = []
for i in range(n - 2):
    if arr[i] > 0:
        break
    if i > 0 and arr[i] == arr[i - 1]:
        continue
    l, r = i + 1, n - 1
    while l < r:
        s = arr[i] + arr[l] + arr[r]
        if s == 0:
            out.append(f"{arr[i]} {arr[l]} {arr[r]}")
            l += 1; r -= 1
            while l < r and arr[l] == arr[l - 1]:
                l += 1
            while l < r and arr[r] == arr[r + 1]:
                r -= 1
        elif s < 0:
            l += 1
        else:
            r -= 1
print("\n".join(out) if out else "None")
