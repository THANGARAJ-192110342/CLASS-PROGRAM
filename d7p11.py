limit=int(input("Enter the limit..:"))
if limit>=0:
    for i in range(0, limit + 1):
        count=1
        for j in range(0, i):
            print(count, end=" ")
            count+=1
        print("\r")
else:
    print("Enter a positive limit..!")