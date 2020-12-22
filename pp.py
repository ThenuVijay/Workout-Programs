no=int(input("Enter no:"))
count=0
while no>0:
    print(no%10,end='')
    no=no//10
    count+=1