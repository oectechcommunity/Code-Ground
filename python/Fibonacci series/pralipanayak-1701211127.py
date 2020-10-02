range1=int(input("Enter how many numbers you want in the fibonacci series:"))
a=0
b=1
for i in range(range1):
    print(a)
    c=a+b
    a=b
    b=c
