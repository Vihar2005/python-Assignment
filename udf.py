def oddeven(a):
    if a%2==0:
        print(a," is even")
    else:
        print(a," is odd")
def maxoftwo(a,b):
    if a>b:
        print(a," is max")
    else:
        print(b," is max")
def maxofthree(a,b,c):
    if a>b:
        if a>c:
            print(a," is max")
        else:
            print(c," is max")
    elif b>c:
        print(b," is max")
    else:
        print(c," is max")
def prime(a):
    if a%2!=0:
        for i in range(3,int(a/2)+1,2):
            if a%i==0:
                print(a," is not prime")
                break
            else:
                print(a," is prime")
        else:
            print(a," is not prime")

def fibonacci(n):
    a,b=0,1
    while b<n:
        print(b,end=" ")
        a,b=b,a+b
    print()
