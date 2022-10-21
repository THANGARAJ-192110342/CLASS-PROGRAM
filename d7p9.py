n=4
l1=[]
sum=0
print("Enter pyhton-C_program-Mathematics-Physics mark: ")
for i in range(0,4):
    val=float(input())
    l1.append(val)
    sum+=val
print("Total: ",sum)
agg=(sum/n)
print("Aggregate: ",agg)
if agg>=75:
    print("Distinction")
elif agg>=60 and agg<75:
    print("First Division")
elif agg>=50 and agg<60:
    print("Second Division")
elif agg>=40 and agg<50:
    print("Third Division")
else:
    print("Fail")
