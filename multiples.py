no=int(input("Enter no:"))
count=int(input("How many times:"))
while count>=1:
   print(no)
   no+=3
   count-=1
    
    
    
 #Least Common Multiples   
no1=int(input("Enter num"))
no2=int(input("Enter num"))  
if no1>no2:
   big=no1
else:
   big=no2
#big=no1 if no1>no2 else no2     (Ternary operator)  
while True:    
    if big%no1==0 and big%no2==0:
        print("LCM",big)
        break
    big+=1    
    
    
 #5 common multiples of given numbers   
no1=int(input("Enter num:"))
no2=int(input("Enter num:"))  
big=no1 if no1>no2 else no2
big2=big   
count=5
#big=no1 if no1>no2 else no2     (Ternary operator)  
while count>=1:    
    if big%no1==0 and big%no2==0:
        print("common multiple is",big)
    big=big+big2
    count-=1    