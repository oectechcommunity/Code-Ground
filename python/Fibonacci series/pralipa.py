def recur_fibo(n):
        if n<=1:
                return n
        else:
                return(recur_fibo(n-1)+recur_fibo(n-2))
len=int(input("Enter the length of your fibonacci series: "))
if len<=0:
        print("please enter a positive integer")
else:
        print("fibonacci sequence: ")
for i in range(len):
        print(recur_fibo(i))                                          
