N=int(input())
can_buy=[]
for i in range(N):
    A, P, X=map(int, input().split())
    zaiko=X-A
    if zaiko>0:
        can_buy.append(P)
    else:
        continue
if len(can_buy)>0:
    print(min(can_buy))
else:
    print(-1)