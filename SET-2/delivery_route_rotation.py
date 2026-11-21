n, k = map(int, input().split())
arr = list(map(int, input().split()))
def rev(l, r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
k %= n
if k > 0:
    rev(0, n - 1)
    rev(0, k - 1)
    rev(k, n - 1)
print(" ".join(map(str, arr)))
