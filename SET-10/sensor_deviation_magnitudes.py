n = int(input())
arr = list(map(int, input().split()))
res = [0] * n
l, r, pos = 0, n - 1, n - 1
while l <= r:
    lsq = arr[l] * arr[l]
    rsq = arr[r] * arr[r]
    if lsq > rsq:
        res[pos] = lsq
        l += 1
    else:
        res[pos] = rsq
        r -= 1
    pos -= 1
print(" ".join(map(str, res)))
