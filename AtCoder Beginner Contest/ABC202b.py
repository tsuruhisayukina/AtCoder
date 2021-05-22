S = list(input())
ans = []
for s in S:
    if s == "6":
        ans.insert(0, "9")
    elif s == "9":
        ans.insert(0, "6")
    else:
        ans.insert(0, s)
print(''.join(ans))