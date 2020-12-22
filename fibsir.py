# f,s=-1,1
# count=int(input("Enter max range"))
# while count>0:
    # t=f+s                                                    #0 1 1 2 3 5 8 13 21 34
    # print(t,end=' ')
    # f=s
    # s=t
    # count-=1
    
    
f,s=-1,1
count=int(input("Enter max range"))
while True:
    t=f+s                                                    
    print(t,end=' ')
    if t==count:
        break
    f=s
    s=t