num=input('Enter a number')
order=len(str(num))

sum=0
record=num
while record>0:
  digit=record%10
  sum += digit**order
  record //= 10
if num == sum:
  print 'i am armstrong'
else:
  print 'i am not'
