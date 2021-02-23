N=int(input())
l=[]
result=0
for i in range(N):
    D1, D2=map(int, input().split())
    if D1==D2:
        l.append(i)
for i in range(1, len(l)):
    if l[i]==l[i-1]+1:
        result+=1
    else:
        result=0
    if result==2:
        print("Yes")
        exit()
print("No")
    