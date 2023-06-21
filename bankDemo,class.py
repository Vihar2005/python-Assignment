class Bank:

    def openAccount(self,cname,acno,balance):
        self.c=cname
        self.ac=acno
        self.b=balance
        print("hello ",self.c,",Your Account Number ",self.ac," Is Opened With ",self.b," Rs.")
    def deposit(self,amount):
        self.b=self.b+amount
    def withdraw(self,amount):
        if amount<=self.b:
            self.b=self.b-amount
        else:
            self.needs=amount-self.b
            print("Sorry You Need Another ",self.needs,"Rs. To Withdraw")
    def checkBalance(self):
        print("Current Balance : ",self.b)

b1=Bank()
cname=input("Enter Customer Name : ")
acno=int(input("Enter Account Number : "))
balance=int(input("Enter Initial Balance : "))
b1.openAccount(cname,acno,balance)

while True:

    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choise=int(input("Enter Your Choice : "))

    if choice==1:
        amount=int(input("Enter deposit Amount : "))
        b1.deposit(amount)
    elif choice==2:
        amount=int(input("Enter withdrawal Amount : "))
        b1.withdraw(amount)
    elif choise==3:
        b1.checkBalance()
    else:
        print("Thank You For Using Our Services.Good Bye")
        break
