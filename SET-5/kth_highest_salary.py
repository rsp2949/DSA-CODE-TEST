n, k = map(int, input().split())
arr = list(map(int, input().split()))
target = n - k
lo, hi = 0, n - 1
while lo <= hi:
    pivot = arr[(lo + hi) // 2]
    lt, i, gt = lo, lo, hi
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1; i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    if target < lt:
        hi = lt - 1
    elif target > gt:
        lo = gt + 1
    else:
        print(arr[target])
        break
