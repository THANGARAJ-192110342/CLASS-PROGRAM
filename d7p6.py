cp=0
try:
    row = int(input("Enter the no.row: "))
except:
    cp=1

if cp==0:
    if row==0:
        print("Enter row greater than zero...!")
    elif row<0:
        print("Enter row value greater than zero...!")
    elif row>0:
        count = 1
        for i in range(0, row + 1):
            for j in range(0, i):
                print(count, end=" ")
                count += 1
            print("\r")
elif cp==1:
    print("Invalid input...!")
