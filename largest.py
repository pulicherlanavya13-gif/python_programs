a=input()
x,y,z=a.split(",")
num1=int(x)
num2=int(y)
num3=int(z)
if num1>num2:
    if num1>num3:
       print("num1 is largest")
    else:
        print("num3")
else:
    if num2>num3:
        print("num2")
    else:
        print("num3")