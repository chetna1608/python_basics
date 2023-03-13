def anagram(str1,str2):
    n1=len(str1)
    n2=len(str2)
    flag=0
    if(n1!=n2):
        flag=0
    else:
        for i in range(0,n1):
            for j in range(0,n2):
                if(str1[j]==str2[i]):
                    flag=1
                    break
                else:
                    flag=0
    if(flag==0):              
        print('not a anagram')
    else:
        print('anagram')
def main():
    str1=input('Enter a string:')
    str2=input('Enter a string:')
    anagram(str1,str2)
if __name__=='__main__':
    main()
                
