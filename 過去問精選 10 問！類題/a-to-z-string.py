s = list(input())
A_index = 0
Z_index = len(s) - 1
for i in range(len(s)):
    if s[i] == "A":
        A_index = i
        break
for i in range(len(s)-1, -1, -1):
    if s[i] == "Z":
        Z_index = i
        break
ans = Z_index - A_index + 1
print(ans)