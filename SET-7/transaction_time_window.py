n = int(input())
arr = list(map(int, input().split()))
x = int(input())
def find_bound(first):
    lo, hi, res = 0, n - 1, -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == x:
            res = mid
            if first:
                hi = mid - 1
            else:
                lo = mid + 1
        elif arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return res
print(find_bound(True), find_bound(False))
