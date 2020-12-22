#count=0
#while count<3:
#    num=int(input("Enter num: "))
 #   num1=int(input("Enter num: "))
  #  num2=num 
  #  num=num1
   # num1=num2
   #   print(num,num1)
   #  count=count+1
   

   
   
   
tot=int(input("Enter number:"))
count=0
while count<=tot:
    ms=input("Enter your maritial status: ")
    if ms=='single':
        age=int(input("Enter your age: "))
        if age>=25 and age<=30:
            gender=input("enter your gender: ")
            if gender=='male':
                print("Groom is ready for marriage")
            else:
                print("Bride is ready for marriage")
        else:
            print("You are not eligible")
    else:
        print("you are married")
    count=count+1            
           
        

