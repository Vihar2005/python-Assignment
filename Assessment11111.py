# Emety dict (to store the data and perform crud opretion on it) ............................................

data_dict = {}

class studentmanagementsys:
    
    
    
    def __init__(self) -> None:
        print("1. press for counsellor")
        print("2. press for faculty")
        print("3. press for student")
        print("4. press for exit...")
        print('\n\n')


       
while True:

    a1 = studentmanagementsys()
    id = int(input("Enter a role id :"))
    
    
 # id gives a condition  which student opretion do  you want to perform.....................................................


    if id==1:
        print("1. Add student:")
        print("2. Remove student")
        print("3. View all student")
        print("4. Press for exit...")
        print("\n\n")
        choice= int(input("Enter your choice : "))
       
        #  give you a choice which opretion do you want to perform ......................
        count=0
        if choice==1:
            for i in range(40):
                serial = int(input("Enter your serial no. : "))
                fname = input("Enter first Name : ")
                lname = input("Enter last Name : ")
                contect = int(input("Enter your contect no .:"))
                faculty = input("Enter your faculty : ")
                subject =input("Enter your subject Name :")
                marks =int(input("Enter your marks : "))
                fees = int(input("Enter your fees :"))
                subject2 =input("Enter your subject Name :")
                marks2 =int(input("Enter your marks : "))
                fees2 = int(input("Enter your fees :"))
                list = []
                list.append(serial)
                for i in list:
                    data_dict[i] = {"fname":fname,"lname":lname,"contect":contect,"faculty": faculty,"subject":[]}
                    data_dict[i]["subject"] ={subject:{"marks1":marks,"fees1":fees},subject2: {"marks":marks2,"fees":fees2}}
                print(data_dict)
                print("\n\n")
            
                exit = input("do you want to any other opreation(y/n) : ")
                print("\n\n")
                if exit == 'n':
                    break
            
        
        elif choice==2:
            
            serial=int(input("Write serial no :"))
            print("\n\n")
            del data_dict[serial]
            print("student detail deleted successfully.")
            print(data_dict)
            print("\n\n")
        

        elif choice ==3:
            print("\n\n")
            print(data_dict)
            print("\n\n")


        else:
            break
    
    elif id==2:
            while True:
                
                print("1.Add marks to the student \n2.View all student")
                choice2 = int(input("Enter your faculty choice : "))

                if choice2== 1:
                    serial = input("Enter serial no of student")
                    

                    subject =input("Enter subject 1 name you want to add marks :")
                    subject2 =input("Enter subject 2 name you want to add marks :")
                    marks = input("Enter subject 1 marks : ")
                    marks2= input("Enter subject 2 marks : ")
                    print("\n\n")
                    data_dict = {serial:{"fname":fname,"lname":lname,"contect":contect,"subject":{}}}    
                    data_dict[serial]["subject"] ={subject:{"marks1":marks,"fees1":fees},subject2: {"marks":marks2,"fees":fees2}}
                    print(data_dict)
                    print("\n\n")
                    exit= input("Do you want to do another opreation (y/n)")
                    
                    if exit =='n':
                        break
                
                    else:
                        continue 
                elif choice2==2:
                    print(data_dict) 
                        
    elif id ==3:
        while True:
            serial =int(input("Enter your serial no :"))
            if serial in data_dict:
                print(data_dict)
                exit =input("Do you want to see another data(y/n) :")
                if exit == 'y':
                    continue
                else:
                    break
            else:
                break    
    
    elif id==4:
        print("\n\n")
        exit=input("Do you want  to add another opreation (y/n) : ")

        if  exit=='y':
          print("\n\n")
          break

