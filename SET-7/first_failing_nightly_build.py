n = int(input())
arr = list(map(int, input().split()))
lo, hi = 0, n - 1
ans = -1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if arr[mid] == 1:
        ans = mid + 1
        hi = mid - 1
    else:
        lo = mid + 1
print(ans)
