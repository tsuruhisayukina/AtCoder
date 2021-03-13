N, M, Q=map(int, input().split())
W_l=[]
V_l=[]
for i in range(N):
    W, V=map(int, input().split())
    W_l.append(W)
    V_l.append(V)

X=list(map(int, input().split()))

for i in range(Q):
    L, R=map(int, input().split())
    if R-L+1==M:
        print(0)
        continue
    if L==R:
        
