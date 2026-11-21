n = int(input())
prices = list(map(int, input().split()))
T = int(input())
seen = {}
for i in range(n):
    rem = T - prices[i]
    if rem in seen:
        print(seen[rem], i)
        break
    seen[prices[i]] = i
