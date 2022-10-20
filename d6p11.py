l1=[]

n=int(input("Enter the limit: "))

for i in range(0,n):
    val=int(input())
    l1.append(val)

p_count=0
c_count=0

for i in l1:
    count = 0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count>2:
        c_count+=1
    else:
        p_count+=1

print("Prime_no: ",p_count)
print("Composite_no: ",c_count)
