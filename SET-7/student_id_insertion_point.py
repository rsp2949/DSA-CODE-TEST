n = int(input())
arr = list(map(int, input().split()))
t = int(input())
lo, hi = 0, n
while lo < hi:
    mid = lo + (hi - lo) // 2
    if arr[mid] < t:
        lo = mid + 1
    else:
        hi = mid
print(lo)
