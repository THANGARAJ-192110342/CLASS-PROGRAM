char=input("Enter the character...:")

limit=int(input("Enter the limit..:"))
if limit>=0:
    for i in range(0, limit + 1):
        for j in range(0, i):
            print(char, end=" ")
        print("\r")
else:
    print("Enter a positive limit..!")