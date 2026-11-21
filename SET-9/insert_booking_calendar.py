import sys
data = sys.stdin.read().split()
n = int(data[0])
ivs = [[int(data[1 + 2 * i]), int(data[2 + 2 * i])] for i in range(n)]
ns, ne = int(data[1 + 2 * n]), int(data[2 + 2 * n])
res = []
i = 0
while i < n and ivs[i][1] < ns:
    res.append(ivs[i])
    i += 1
while i < n and ivs[i][0] <= ne:
    if ivs[i][0] < ns:
        ns = ivs[i][0]
    if ivs[i][1] > ne:
        ne = ivs[i][1]
    i += 1
res.append([ns, ne])
while i < n:
    res.append(ivs[i])
    i += 1
print("\n".join(f"{a} {b}" for a, b in res))
