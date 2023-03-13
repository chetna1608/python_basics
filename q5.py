def gcd(m,n):
    if(m==0):
        return n
    if(n==0):
        return m
    if(m==n):
        return m
    else:
        while(n!=0):
            res=m%n
            if(res==0):
                return n
            else:
                m=n
                n=res
    return res
def main():
    m=int(input("Enter 1st number:"))
    n=int(input("Enter 2nd number:"))
    print("The GCD =",gcd(m,n))
if __name__=='__main__':
    main()
    