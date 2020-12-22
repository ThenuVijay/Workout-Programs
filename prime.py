#common divisors of 100
#100-100 50 25 20 10 5 4 2 
n=100
i=n
while i>=2:
    if n%i==0:
        print (i,end=' ')
    i=i-1      
    
    
#output-->2 4 5 10 20 25 50 100
n=100
i=2
while i<=100:
    if n%i==0:
        print(i)
    i+=1    
    
    
#common divisors of two numbers
#100=2 4 5 10 20 25 50 100
#50 = 2 5 10 25 50    
num1=int(input("enter num:"))
num2=int(input("enter num:"))
if num1>num2:
    small=num1
elif num2>num1:
    small=num2
while small>=2:
    if num1%small==0 and num2%small==0:
        print (small)
    small-=1   


    
    
# greatest common divisors of two numbers
#100=2 4 5 10 20 25 50 100
#50 = 2 5 10 25 50    
num1=int(input("enter num:"))
num2=int(input("enter num:"))
if num1>num2:
    small=num1
elif num2>num1:
    small=num2
while small>=2:
    if num1%small==0 and num2%small==0:
        print ("GCD :",small)
        break    
    small-=1       