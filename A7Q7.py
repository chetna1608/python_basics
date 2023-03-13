name= {0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",}


n = int(input("Enter a number : "))
words=[]
while(n>0):
    rem = n%10
    words.append(name[rem])
    n = n//10


words.reverse()
wordString=""
for i in words:
    wordString = wordString+i+" "


print(wordString)

