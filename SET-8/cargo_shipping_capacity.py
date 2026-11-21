n, D = map(int, input().split())
w = list(map(int, input().split()))
lo = total = 0
for x in w:
    if x > lo:
        lo = x
    total += x
hi = total
while lo < hi:
    mid = lo + (hi - lo) // 2
    days, cur = 1, 0
    for x in w:
        if cur + x > mid:
            days += 1
            cur = x
        else:
            cur += x
    if days <= D:
        hi = mid
    else:
        lo = mid + 1
print(lo)
