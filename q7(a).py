import math
#def print_series(x,n):
def print_series(x):
    term=1
    i=2
    error=0.000001
    sum=1
    #count=1
    #while(count<n):
    while(abs(term)>error):
        term=-1*((x*x)/(i*(i-1))*term)
        sum=sum+term
        #count=count+1
        i=i+2
    print(sum)
x=int(input("Enter x value in radian"))
#n=int(input("Enter n value"))
#print_series(x,n)
print_series(x)
print(math.cos(x))