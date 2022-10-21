l1=[]
min_val=0
max_val=0
size=int(input("tot. no. of elements: "))
for i in range(0,size):
    val=int(input())
    l1.append(val)
n=int(input("Enter nth minimum value...: "))
m=int(input("Enter mth maximum value...: "))

l1.sort()

if n>=0 and n<size:
    min_val=l1[n-1]
else:
    print("N-value is out of bound....!")

if m>=0 and m<size:
    max_val=l1[size-m]
else:
    print("M-value is out of bound...!")

print("Sum: ",max_val+min_val)
print("Difference: ",max_val-min_val)