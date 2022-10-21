
def isPerfect(val):
    sum=0
    if num>=6:
        for i in range(1,num):
            if num%i==0:
                sum+=i
        if sum==num:
            print("Perfect number...!")
        else:
            print("Not a perfect number...!")
        sum=0

    else:
        print("Not a perfect number...!")

cp=0
try:
    num=int(input("Enter the value: "))
except:
    cp=1

if cp==0:
    isPerfect(num)
else:
    print("Invalid input...!")

