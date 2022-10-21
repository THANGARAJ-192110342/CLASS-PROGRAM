cp=0
try:
    age=float(input("Enter age: "))
except:
    cp=1

if cp==0:
    if age>=0:
        if age>=18:
            print("Eligible to vote...!")
        else:
            print("You are allowed to vote after",(18-age),"years")
    if age<0:
        print("Age can't be negative...!")
else:
    print("Invalid Input..!")