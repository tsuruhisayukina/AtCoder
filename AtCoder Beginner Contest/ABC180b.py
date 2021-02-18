N=int(input())
x=list(map(int, input().split()))
m=0
y=0
c=[]
for i in x:
    m+=abs(i)
    y+=abs(i)**2
    c.append(abs(i))
print(m)
y=y**(1/2)
print(y)
print(max(c))

