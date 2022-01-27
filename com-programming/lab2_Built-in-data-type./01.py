a, b = [float(x) for x in input().split()]
imz = complex(a, b) + complex(a, -b)
print(int(imz.real))  if imz.real.is_integer() else print(float(imz.real))