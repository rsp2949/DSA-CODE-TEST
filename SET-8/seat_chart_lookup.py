R, C = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(R)]
t = int(input())
lo, hi = 0, R * C - 1
ans_r, ans_c = -1, -1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    r, c = mid // C, mid % C
    if mat[r][c] == t:
        ans_r, ans_c = r, c
        break
    elif mat[r][c] < t:
        lo = mid + 1
    else:
        hi = mid - 1
print(ans_r, ans_c)
