no=int(input("enter a number:"))
order=len(str(no))
sum1=0
temp=no
while temp>0:
    digit=temp%10
    sum1 += digit ** order
    temp //= 10

if no==sum1:
    print(no,"is an armstrong number")
else:
    print(no,"is not an armstrong number")
           