cp=0


def Add(a,b):
    print("Sum: ",a+b)
def Sub(a,b):
    print("Diff: ",a+b)
def Pow(a,b):
    print("power: ",a**b)
def Mul(a,b):
    print("product: ",a*b)
def Div(a,b):
    print("Result: ",a/b)

try:
    ch=int(input("1)Add\n2)Sub\n3)Pow\n4)Mul\n5)Div\t: "))
    val1=float(input("Enter the 1st value: "))
    val2=float(input("Enter the 2nd value: "))
except:
    cp=1

if cp==0:
    if ch==1:
        Add(val1,val2)
    if ch==2:
        Sub(val1,val2)
    if ch==3:
        Pow(val1,val2)
    if ch==4:
        Mul(val1,val2)
    if ch==5:
        Div(val1,val2)
else:
    print("Invalid Input...!")