m, n = map(int, input().split())
A = list(map(int, input().split())) if m > 0 else []
B = list(map(int, input().split())) if n > 0 else []
i = j = 0
res = []
while i < m and j < n:
    if A[i] < B[j]:
        res.append(str(A[i])); i += 1
    elif B[j] < A[i]:
        res.append(str(B[j])); j += 1
    else:
        res.append(str(A[i])); i += 1; j += 1
while i < m:
    res.append(str(A[i])); i += 1
while j < n:
    res.append(str(B[j])); j += 1
print(" ".join(res))
