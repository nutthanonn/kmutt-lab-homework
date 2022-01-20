v1,v2,v3 = [float(x) for x in input().split()]
u1,u2,u3 = [float(x) for x in input().split()]
v = [v1,v2,v3]
u = [u1,u2,u3]
ans = v1*u1 + v2*u2 + v3*u3
print(ans)