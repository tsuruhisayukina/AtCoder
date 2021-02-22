N, K=input().split()
a=N
for i in range(int(K)):
    g2_list=sorted(a)
    g2=""
    for i in g2_list:
        g2+=i
    intg2=int(g2)
    
    g2_list.sort(reverse=True)
    g1_list=g2_list
    g1=""
    for i in g1_list:
        g1+=i
    intg1=int(g1)
    
    f=(intg1)-(intg2)
    
    
    a=str(f)

print(a)    
