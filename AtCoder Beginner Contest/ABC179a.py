S=input()
l=len(S)
if S[l-1]=="s":
    S+="es"
else:
    S+="s"
print(S)