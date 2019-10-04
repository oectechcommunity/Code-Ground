len=input("enter the length of the fibonacci series")
first_value=0
second_value=1
iteration=0
if len<=0:
        print"provide a number greater then zero"
elif len==1:
        print "1"
else:
        while iteration<len:
                final_value=first_value+second_value
                first_value=second_value
                second_value=final_value
                iteration+=1
        print"fibonacci series is",final_value                                              
