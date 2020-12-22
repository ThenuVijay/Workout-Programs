num1=int(input("Enter num:"))
num2=int(input("Enter num:"))
big=num1 if num1>num2  else num2
while True:
    if big%num1==0 and big%num2==0:
        print("LCM",big)
        break
    big+=1
    