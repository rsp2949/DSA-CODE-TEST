n = int(input())
arr = list(map(int, input().split()))
q = int(input())
lo, hi = 0, n - 1
ans = -1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if arr[mid] == q:
        ans = mid
        break
    elif arr[mid] < q:
        lo = mid + 1
    else:
        hi = mid - 1
print(ans)
