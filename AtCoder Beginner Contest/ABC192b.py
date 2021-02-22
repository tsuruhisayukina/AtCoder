S=input()
S_odd=""
S_even=""

if len(S)==1 and S.islower()==True:
    print("Yes")
    exit()
elif len(S)==1 and S.islower()==False:
    print("No")
    exit()

for i in range(len(S)):
    if i%2==0:
        S_odd+=S[i]
    else:
        S_even+=S[i]

if S_odd.islower()==True and S_even.isupper()==True:
    print("Yes")
else:
    print("No")