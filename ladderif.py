rno=int(input("enter roll no : "))
sname=input("enter student name : ")
s1=int(input("Enter marks of subject 1:"))
s2=int(input("Enter marks of subject 2:"))
s3=int(input("Enter marks of subject 3:"))

total=s1+s2+s3
per=total/3

print("student roll no : ",rno)
print("student name : ",sname)
print("total : ",total)
print("percentage : ",per)

if per>=70:
    print("distinction")
elif per>=60:
    print("first class")
elif per>=50:
    print("second class")
elif per>=40:
    print("first class")
elif per>=30:
    print("pass class")
else:
    print("fail")
