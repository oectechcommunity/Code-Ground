range=input("enter the length of the fibonacci series")
a=0
b=1

while a<range:
  print a,
  c=a+b
  a=b
  b=c
