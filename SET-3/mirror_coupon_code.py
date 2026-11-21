s = input()
l, r = 0, len(s) - 1
ok = True
while l < r:
    if not s[l].isalnum():
        l += 1
    elif not s[r].isalnum():
        r -= 1
    else:
        if s[l].lower() != s[r].lower():
            ok = False
            break
        l += 1
        r -= 1
print("YES" if ok else "NO")
