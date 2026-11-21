n = int(input())
arr = list(map(int, input().split()))
k = 0
for x in arr:
    if k < 2 or x != arr[k - 2]:
        arr[k] = x
        k += 1
print(k)
print(" ".join(str(arr[i]) for i in range(k)))
