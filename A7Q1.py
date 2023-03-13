n=int(input("Enter number of elements in list:"))
list1=[]
for i in range (0,n):
                x=int(input("Enter element"))
                list1.append(x)
list2=[]
for i in list1:
                if i not in list2:
                                list2.append(i)
print(list2)

                
