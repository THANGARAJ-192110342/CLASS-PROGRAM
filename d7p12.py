val=int(input("Enter the number: "))
op=int(input("1)Decimal\n2)Octal: "))

i=1
sum=0
cp=0
while val>0:
    rem=val%10
    if rem==0 or rem==1:
        sum = sum + int(rem * i)
        i *= 2
        val = int(val / 10)
    else:
        cp=1
if cp==0:
    print(sum)
else:
    print("invalid binary value: ")
def binaryToDecimal(n):
    return int(n,2)
num='111011.011'
print(binaryToDecimal(num))