WorkingHour=int(input("Enter your working hours:"))
if WorkingHour<=40:
    salary=WorkingHour*100
    print("Your salary is",salary)
elif ((WorkingHour>40) & (WorkingHour<=100)):
    WH=WorkingHour-40
    salary1=(WH*150)+(40*100)
    print("Your salary is",salary1)
elif WorkingHour>100:
    print("Your OverTime Limit Should not Exceed 60")
    
    
    
emp=int(input("For How Many Employees do you need to calculate salary: "))
i=0
while i<emp:
    WorkingHour=int(input("Enter your working hours:"))
    if WorkingHour<=40:
        salary=WorkingHour*100
        print("Your salary is",salary)
    elif ((WorkingHour>40) & (WorkingHour<=100)):  #WorkingHour-->40 OvertimeLimit-->60 Total=100
        WH=WorkingHour-40
        salary1=(WH*150)+(40*100)
        print("Your salary is",salary1)
    elif WorkingHour>100:
        print("Your OverTime Limit Should not Exceed 60")
    i+=1
print()    
    
    