def replace2(str1):
    str2=''
    n=len(str1)
    for i in range(0,n):
        if(str1[i]!=str1[i-1]):
            str2+=str1[i]
        else:
            str2+='*'
    return str2

def main():
    str1=input('Enter a string:')
    ans=replace2(str1)
    print(ans)
if __name__=='__main__':
    main()
