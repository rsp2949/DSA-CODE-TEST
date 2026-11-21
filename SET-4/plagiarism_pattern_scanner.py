s = input().strip()
p = input().strip()
ns, np = len(s), len(p)
if np > ns:
    print("None")
else:
    need = [0] * 26
    have = [0] * 26
    for i in range(np):
        need[ord(p[i]) - 97] += 1
        have[ord(s[i]) - 97] += 1
    matches = 0
    for i in range(26):
        if need[i] == have[i]:
            matches += 1
    res = []
    if matches == 26:
        res.append("0")
    for i in range(np, ns):
        r = ord(s[i]) - 97
        have[r] += 1
        if have[r] == need[r]:
            matches += 1
        elif have[r] == need[r] + 1:
            matches -= 1
        l = ord(s[i - np]) - 97
        have[l] -= 1
        if have[l] == need[l]:
            matches += 1
        elif have[l] == need[l] - 1:
            matches -= 1
        if matches == 26:
            res.append(str(i - np + 1))
    print(" ".join(res) if res else "None")
