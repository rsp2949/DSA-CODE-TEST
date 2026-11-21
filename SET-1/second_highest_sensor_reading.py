n = int(input())
arr = list(map(int, input().split()))
first = second = None
for x in arr:
    if first is None or x > first:
        second = first
        first = x
    elif x != first and (second is None or x > second):
        second = x
print(second if second is not None else "None")
