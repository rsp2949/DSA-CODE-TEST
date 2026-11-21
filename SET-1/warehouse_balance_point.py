n = int(input())
arr = list(map(int, input().split()))
total = 0
for x in arr:
    total += x
left_sum = 0
ans = -1
for i in range(n):
    if left_sum == total - left_sum - arr[i]:
        ans = i
        break
    left_sum += arr[i]
print(ans)
