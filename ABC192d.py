X=input()
M=int(input())
d=int(max(X))
n=d+1
ans=0
josu=0
shinsu=0
while shinsu<=M:
    shinsu=0
    for i in range(1, len(X)+1):
        shinsu+=int(X[-i])*(n**josu)
        josu+=1
    if shinsu<=M:
        n+=1
        ans+=1
        josu=0
    else:
        print(ans)
        break
    
    
    