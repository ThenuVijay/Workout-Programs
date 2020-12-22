no=int(input("Enter no:"))
count=0
while no>0:
    print(no%10)
    no=no//10
    count+=1
print("Count of digits",count)    


no=int(input("Enter no:"))
count=0
sumofdigits=0
while no>0:
    sumofdigits=sumofdigits+(no%10)
    print(no%10)
    no=no//10
    count+=1
print('Addition of digits',sumofdigits)    
print("Count of digits",count)    


#1234
#0+4=4
#4+3=7
#7+2=9
#9+1=10

#1234-palindrome
#0*10+4=4
#4*10+3=43
#43*0+2=432
#432*10+1=4321

#palindrome number
no=int(input("Enter no:"))           #1234
no2=no
count=0
sumofdigits=0
while no>0:
    sumofdigits=(sumofdigits*10)+(no%10)
    print(no%10)
    no=no//10
    count+=1
print('Reverse value is',sumofdigits)
if no2==sumofdigits:
        print("Palindrome")
else:
    print("Not palindrome")
print("Count of digits",count)    


#Armstrong number
no=int(input("Enter no:"))
no2=no
armstrong=0
while no>0:
    rem=no%10
    armstrong=armstrong+(rem*rem*rem)
    no=no//10
if no2==armstrong:
        print("Armstrong")
else:
    print("Not Armstrong")
  


