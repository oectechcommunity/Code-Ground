// Python2

bin=input('Enter a binary number:')
dec=0
base=1
while bin>0:
  rem=bin%10
  dec=dec+rem*base
  base=base*2
  bin=bin/10
print dec
