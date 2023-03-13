def capitals(str1):
    n1=len(str1)
    for j in range(0,n1):
        str2=''
        if(ord(str1[0])>=97 and ord(str1[0])<=122):
            str2=str2+chr(ord(str1[0])-32)
        else:
            str2=str2+str1[0]
        n1=len(str1)
        for i in range(0,n1-1):
            if(ord(str1[i])==32):
                str2=str2+' '
                if(ord(str1[i+1])>=97 and ord(str1[i+1])<=122):
                    str2=str2+chr(ord(str1[i+1])-32)
                    continue
                else:
                    str2=str2+str1[i+1]
                    continue
            else:
                i=i+1
                if(ord(str1[i])>=65 and ord(str1[i])<=90):
                   str2=str2+chr(ord(str1[i])+32)
                else:
                    str2=str2+str1[i]
        return str2
str1=input('Enter string')
print(capitals(str1))
  
