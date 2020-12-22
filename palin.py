#print palindrome
num=input("Enter no")
reverse=''
i=len(num)-1
while i>=0:
    reverse=reverse+num[i]
    i-=1
print(reverse)
#print(num)
if num==reverse:
    print("palindrome")
else:
    print("Not palindrome")
        
#print palindrome
no=input("Enter no")
reverse=' '
i=len(no)-1
while i>=0:
        print(no[i],end=' ')
        # reverse=reverse+no[i]
        i-=1
# print(reverse) 
# if no==reverse:
     # print("palindrome")
# else:
     # print("Not palindrome")       
     
     