def count_words(str1):
    n1=len(str1)
    count=1
    for i in range(0,n1):
        if(str1[i]==' '):
            count=count+1
    return count
def main():
    str1=input('Enter a sentence:')
    print('No. of words in the sentence=',count_words(str1))
    
if __name__=='__main__':
    main()
