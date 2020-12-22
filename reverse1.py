no="1234"
i=len(no)-1
while i>=0:
    print(no[i])
    i-=1
 

#print sum of digits 
no=input("Enter no")
sumofdigits=0
i=len(no)-1
while i>=0:
        sumofdigits=sumofdigits+int(no[i])
        i-=1
print(sumofdigits)        


#print reverse
no=input("Enter no")
reverse=' '
i=len(no)-1
while i>=0:
        reverse=reverse+no[i]
        i-=1
print(reverse) 

        
        
        
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
     
     
     
     
# #print palindrome
# name=input("Enter name:")
# reverse=' '
# i=len(name)-1
# while i>=0:
        # reverse=reverse+name[i]
        # i-=1
# print(reverse) 
# if name==reverse:
     # print("palindrome")
# else:
     # print("Not palindrome")       
         
     