l1=[]
cp=0
n=int(input("Enter the limit: "))

try:
    print("Enter the data: ")
    for i in range(0, n):
        val = float(input())
        l1.append(val)
except:
    cp=1

if cp==0:
    p_count = 0
    c_count = 0

    for i in l1:
        count = 0
        for j in range(1, int(i) + 1):
            if i % j == 0:
                count += 1
        if count > 2:
            c_count += 1
        else:
            p_count += 1

    print("Prime_no: ", p_count)
    print("Composite_no: ", c_count)
elif cp==1:
    print("Invalid input...!")
