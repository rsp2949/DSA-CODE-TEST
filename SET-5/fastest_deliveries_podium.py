n, k = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(k):
    min_idx = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
print(" ".join(str(arr[i]) for i in range(k)))
