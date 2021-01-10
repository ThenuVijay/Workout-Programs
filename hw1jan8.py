
#Armstrong Using Recursive Function
num1=0
def armstrong(num):
    if num==0:
        return 0
    else:
        rem=num%10
        global num1
        num1=num1+(rem*rem*rem)
        armstrong(num//10)
        return num1       
        
num=int(input("Enter num:"))       
result=armstrong(num)
if result==num:
    print("Armstrong")
else:
    print("Not Armstrong ")      


#fibanocci using recursive function
first=-1
second=1
def fibanocci(count):
    if count==0:
        return
    else:
       global first
       global second 
       print(first+second)
       second=second+first
       first=second-first
       fibanocci(count-1)
       
       
fibanocci(5)      

#Palindrome using Recursive function:    

def reverse(name):
    l= len(name)
    if (l == 0):
        return
    else:
        last_letter = name[l-1]
        print(last_letter,end=" ")
        reverse(name[0:l-1])

name=input("Enter Name")
r=reverse(name)
if r==name:
    print("Palindrome")
else:
    print("Not Palindrome")
    


#Gcd using Recursive function
def gcd(small):
    if small==1:
        return 
    else:
        if(num1%small==0 and num2%small==0):
            print(small)
    gcd(small-1)

num1=int(input("enter num:"))
num2=int(input("enter num:"))
small=num1 if num2>num1 else num2
gcd(small)    


#LCM  using Recursive Function
num1=int(input("Enter num:"))
num2=int(input("Enter num:"))    
big=num1 if num1>num2  else num2
def lcm(big):    
    while True:
        if big%num1==0 and big%num2==0:
            print("LCM",big)
            break
        lcm(big+1)    
        
lcm(big)        
       