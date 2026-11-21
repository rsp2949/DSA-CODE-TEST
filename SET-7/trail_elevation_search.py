n = int(input())
arr = list(map(int, input().split()))
h = int(input())
lo, hi = 0, n - 1
while lo < hi:
    mid = lo + (hi - lo) // 2
    if arr[mid] < arr[mid + 1]:
        lo = mid + 1
    else:
        hi = mid
peak = lo
def bsearch(l, r, asc):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == h:
            return mid
        if (arr[mid] < h) == asc:
            l = mid + 1
        else:
            r = mid - 1
    return -1
ans = bsearch(0, peak, True)
if ans == -1:
    ans = bsearch(peak + 1, n - 1, False)
print(ans)
