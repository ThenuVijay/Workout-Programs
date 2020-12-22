no=int(input("Enter no:"))
binary=''
while no>0:
    rem=no%2
    binary=str(rem)+binary
    # print(rem,end='')
    no=no//2
else:
    print(binary)