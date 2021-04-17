import math
X, Y, Z = map(int, input().split())
T_1g = Y / X
ans = math.ceil(T_1g * Z -1)

print(ans)
