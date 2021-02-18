N=int(input())
result=[]
i=1
while i*i<=N:
    if N%i==0:
        result.append(i)
        result.append(int(N/i))
    i+=1
new_result=set(result)
up_result=list(sorted(new_result))
for j in up_result:
    print(j)