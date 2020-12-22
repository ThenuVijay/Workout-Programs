first = -1 
second = 1
count = int(input("Enter number "))
while count>0:
	print(first+second)
	second = first + second
	first = second - first
	count-=1
