n = int(input())
arr = list(map(int, input().split()))
passes = 0
for i in range(n - 1):
    swapped = False
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    if swapped:
        passes += 1
    else:
        break
print(" ".join(map(str, arr)))
print(passes)
