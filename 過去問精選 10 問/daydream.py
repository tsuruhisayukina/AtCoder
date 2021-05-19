# S = list(input())
# S = reversed(S)
# S = ''.join(S)
# T = ["maerd", "remaerd", "esare", "resare"]
# t = ""
# for s in S:
#     t += s
#     if t in T:
#         S = S.replace(t, '')
#         t = ""
#         text = []
# if S == '':
#     print("YES")
# else:
#     print("NO")

s=input().replace("eraser","").replace("erase","").replace("dreamer","").replace("dream","")
print("YES" if len(s)==0 else "NO")
    