n = int(input())
arr = list(map(int, input().split()))
t = int(input())
lo, hi, ans = 0, n - 1, -1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if arr[mid] == t:
        ans = mid
        break
    if arr[lo] <= arr[mid]:
        if arr[lo] <= t < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    else:
        if arr[mid] < t <= arr[hi]:
            lo = mid + 1
        else:
            hi = mid - 1
print(ans)
