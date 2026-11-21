n, m = map(int, input().split())
pages = list(map(int, input().split()))
if m > n:
    print(-1)
else:
    lo = total = 0
    for p in pages:
        if p > lo:
            lo = p
        total += p
    hi = total
    while lo < hi:
        mid = lo + (hi - lo) // 2
        groups, cur = 1, 0
        for p in pages:
            if cur + p > mid:
                groups += 1
                cur = p
            else:
                cur += p
        if groups <= m:
            hi = mid
        else:
            lo = mid + 1
    print(lo)
