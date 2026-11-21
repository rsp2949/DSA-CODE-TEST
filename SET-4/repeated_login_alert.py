n, k = map(int, input().split())
arr = list(map(int, input().split()))
window = set()
alert = False
for i in range(n):
    if arr[i] in window:
        alert = True
        break
    window.add(arr[i])
    if len(window) > k:
        window.remove(arr[i - k])
print("YES" if alert else "NO")
