N, K = map(int, input().split())
money = {}
for i in range(N):
    A, B = map(int, input().split()) 
    if A in money:
        money[A] += B
        continue
    money[A] = B

position = K
K = 0
for i in sorted(money):
    position += K
    K = 0
    if position >= i:
        K += money[i]
    else:
        break
print(position + K)