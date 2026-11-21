n = int(input())
arr = list(map(int, input().split()))
def merge_count(a):
    m = len(a)
    if m <= 1:
        return a, 0
    mid = m // 2
    L, invL = merge_count(a[:mid])
    R, invR = merge_count(a[mid:])
    merged = []
    i = j = 0
    inv = invL + invR
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            merged.append(L[i])
            i += 1
        else:
            merged.append(R[j])
            inv += len(L) - i
            j += 1
    while i < len(L):
        merged.append(L[i]); i += 1
    while j < len(R):
        merged.append(R[j]); j += 1
    return merged, inv
_, ans = merge_count(arr)
print(ans)
