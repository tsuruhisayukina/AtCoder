H, W, X, Y = map(int, input().split())
X -= 1
Y -= 1
Y_l = []
ans = 0
for i in range(H):
    S = list(input())
    if i == X:
        X_l = S
    for j in range(len(S)):
        if j == Y:
            Y_l.append(S[j])

for i in X_l[Y:]:
    if i == ".":
        ans += 1
    if i == "#":
        break
for i in reversed(X_l[:Y]):
    if i == ".":
        ans += 1
    if i == "#":
        break
for i in Y_l[X:]:
    if i == ".":
        ans += 1
    if i == "#":
        break
for i in reversed(Y_l[:X]):
    if i == ".":
        ans += 1
    if i == "#":
        break
print(ans-1)