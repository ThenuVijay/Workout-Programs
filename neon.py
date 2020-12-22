# neon number---->9^2=81-->8+1=9
num=int(input("Enter num: "))
sqr=num**2
total=0
#print(sqr)
while sqr>0:
    total=total+sqr%10
    sqr=sqr//10
#print(total)
if num==total:
    print("Neon number")
else:
    print("Non Neon Number")
   

    