n = int(input())
arr = list(map(int, input().split()))
stack = [(0, n - 1)]
while stack:
    lo, hi = stack.pop()
    if lo >= hi:
        continue
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
    stack.append((lo, lt - 1))
    stack.append((gt + 1, hi))
print(" ".join(map(str, arr)))
