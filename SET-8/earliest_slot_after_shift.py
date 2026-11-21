n = int(input())
arr = list(map(int, input().split()))
lo, hi = 0, n - 1
while lo < hi:
    mid = lo + (hi - lo) // 2
    if arr[mid] > arr[hi]:
        lo = mid + 1
    else:
        hi = mid
print(arr[lo])
