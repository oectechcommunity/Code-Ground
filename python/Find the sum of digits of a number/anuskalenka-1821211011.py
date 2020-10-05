#Write a program to find sum of digits of a number
#Input : A number
#Output : sum of digits
no = int(input("enter the number"))
sum = 0
while no>0:
    digit = no % 10
    sum = sum+digit
    no = no//10
print("the sum of the digits of a no is",sum)

