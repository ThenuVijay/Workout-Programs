# import math
# no=int(input("enter no:"))
# power=int(input("enter power"))
# print(int(math.pow(no,power)))

import math
no=int(input("Enter binary"))
decimal=0
i=0
while no>0:
    rem=no%10
    value=rem*int(math.pow(2,i))
    decimal=decimal+value
    no=no//10
    i+=1
else:
    print(decimal)