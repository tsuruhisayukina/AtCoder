N=int(input())
A_list=list(map(int, input().split()))
gcd=0
gcd_list=[]
k=2
while True:
    for i in A_list:
        if i%k==0:
            gcd+=1
    gcd_list.append(gcd)
    gcd=0
    if k==max(A_list):
        break
    else:
        k+=1
print(gcd_list.index(max(gcd_list))+2)       