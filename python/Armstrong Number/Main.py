# Python2

no=input('Enter a number')
record=no
count=0
while no>0:
  no=no/10
  count+=1
no=record
sum=0
while no>0:
  last=no%10
  sum=sum+last**count
  no=no/10
no=record
if sum==no
  print 'i am armstrong'
else:
  print 'i am not an armstrong'
