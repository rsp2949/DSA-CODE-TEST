n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    val = arr[i] if arr[i] > 0 else -arr[i]
    if arr[val - 1] > 0:
        arr[val - 1] = -arr[val - 1]
missing = []
for i in range(n):
    if arr[i] > 0:
        missing.append(str(i + 1))
print(" ".join(missing) if missing else "None")
