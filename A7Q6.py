def nlist():
                n=int(input("Enter number of lists"))
                list1=[]
                
                for i in range(0,n):
                                
                                ilist=[]
                                for j in range(1,6):
                                                
                                                ilist.append((i+1)*j)
                                               
                                list1.append(ilist)                
                                
                print(list1)
nlist()
