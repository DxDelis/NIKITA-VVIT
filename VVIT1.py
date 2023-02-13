a=int(input())
b=int(input())
c=int(input())
D=b**2-4*a*c
if D<0:
    print("korney net")
else:
    x1=(-b+D**0.5)/2*a
    x2=(-b-D**0.5)/2*a
    if x1==x2:
        print("korney yr",x1)
    else:
        print("korney yr",x1,x2)