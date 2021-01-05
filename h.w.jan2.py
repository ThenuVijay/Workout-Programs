#With sort() function

l=['vishnu','bala','harish','joshi']
l1=[11.2,17.2,18,12]
l2=l1.copy()
l2.sort()
for i in range(len(l2)):
    for j in range(len(l1)):
        if l2[i]==l1[j]:
            print(l[j],l2[i])
print()        

#Without sort() function

l=['vishnu','bala','harish','joshi']
l1=[11.2,17.2,18,12]
l2=l1.copy()
l3=[]
while l2:
    min = l2[0]  
    for x in l2: 
        if x < min:
            min = x
    l3.append(min)
    l2.remove(min)    
for i in range(len(l3)):
    for j in range(len(l1)):
        if l3[i]==l1[j]:
            print(l[j],l3[i])
print()  