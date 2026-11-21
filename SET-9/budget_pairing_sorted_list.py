n = int(input())
arr = list(map(int, input().split()))
T = int(input())
l, r = 0, n - 1
while l < r:
    s = arr[l] + arr[r]
    if s == T:
        print(l + 1, r + 1)
        break
    elif s < T:
        l += 1
    else:
        r -= 1
