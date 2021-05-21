s = list(input())
t = list(input())
s_dash = ''.join(sorted(s))
t_dash = ''.join(sorted(t, reverse=True))
if s_dash < t_dash:
    print("Yes")
else:
    print("No")