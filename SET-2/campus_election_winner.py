n = int(input())
arr = list(map(int, input().split()))
cand, count = 0, 0
for x in arr:
    if count == 0:
        cand = x
    count += 1 if x == cand else -1
print(cand)
