A, B, C, X, Y = map(int, input().split())
piza_a = 0
piza_b = 0
A_piza_Bpiza_total = A * X + B * Y
Cpiza_only_total = C * max(X, Y) * 2
if X > Y:
    ABCpiza_total = C * Y * 2 + A * (X - Y)
else:
    ABCpiza_total = C * X * 2 + B * (Y - X)
ans = min(A_piza_Bpiza_total, Cpiza_only_total, ABCpiza_total)
print(ans)
