import udf

while True:

    print("*"*50)
    print("1. oddeven")
    print("2. maxofTwe")
    print("3. maxofthree")
    print("4. prime")
    print("5. fibonacci")
    print("6. Exit")
    print("*"*50)
    choice=int(input("Enter your choice : "))
    print("*"*50)

    if choice==1:
        a=int(input("Enter value : "))
        udf.oddeven(a)
        print("*"*50)
    elif choice==2:
        a=int(input("enter value : "))
        b=int(input("enter value : "))
        udf.maxoftwo(a,b)
        print("*"*50)
    elif choice==3:
        a=int(input("enter value : "))
        b=int(input("enter value : "))
        c=int(input("enter value : "))
        udf.maxofthree(a,b,c)
        print("*"*50)
    elif choice==4:
        a=int(input("enter value : "))
        udf.prime(a)
        print("*"*50)
    elif choice==5:
        a=int(input("enter value : "))
        udf.fibonacci(a)
        print("*"*50)
    elif choice==6:
        print("thanks for using our services")
        print("*"*50)
        break
    else:
        print("Invalid choise")
        print("*"*50)



    
