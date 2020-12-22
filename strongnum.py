num=int(input("enter num:"))
num1=num
#fact=1
sumofdigits=0
print(num)
while num>0:
    i=num%10
    fact=1
    print(i)
    while i>0:
        fact=fact*i
        print(fact)
        i-=1
    sumofdigits=sumofdigits+fact
    print(sumofdigits)
    num=num//10
print(num1)
print(sumofdigits)
if num1==sumofdigits:
        print("Strong number")
else:
        print("Not Strong number")
        
    
    