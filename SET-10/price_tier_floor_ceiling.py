n = int(input())
arr = list(map(int, input().split()))
q = int(input())
lo, hi, flr = 0, n - 1, None
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if arr[mid] <= q:
        flr = arr[mid]
        lo = mid + 1
    else:
        hi = mid - 1
lo, hi, ceil = 0, n - 1, None
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if arr[mid] >= q:
        ceil = arr[mid]
        hi = mid - 1
    else:
        lo = mid + 1
print(flr if flr is not None else "None", ceil if ceil is not None else "None")
