no=input('Enter a no:')
record=no

count=0
while no>0:
  no=no/10
  count +=1
  
no=record
sum=0
while no>0:
  last=no%10
  sum=(sum+last)**count
  no=no/10
  
no=record
if sum==no:
  print'i am Armstrong'
else:
  print'i am not'
