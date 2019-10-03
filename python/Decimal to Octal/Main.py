#Python2

dec=input('Enter a decimal no:')
octal=0
base=1
while dec>0:
  rem=dec%8
  octal=octal+rem*base
  base=base*10
  dec=dec/8
print octal
