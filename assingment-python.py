

# 1. What is File function in python? What is keywords to create and write file.
# Python file object provides methods and attributes to access and manipulate files. Using file objects, we can read or write any files. 
# the keywod to create file is open() and for write file  file.write() 
# ex file = open("newfile.txt","w")
    #file.write(" my new file...")



# 2 Write a Python program to read an entire text file.


file = open("file.txt","w")
file.write("this is my new file" )
file.close()

file = open("file.txt","r")
print(file.read())
file.close()




# 3 Write a Python program to append text to a file and display the text.

file = open("tops1.txt","w")
file.write("this is file  input //output demo using python ")
file.close()
print("file written successfully")

file = open("tops1.txt","r")

print(file.read())
file.close

file = open("tops1.txt","a")
file.write("\nnow this file is appended")

file.close()


file= open("tops1.txt","r")
print(file.read())
file.close()




#4  Write a Python program to read first n lines of a file.

n = int(input("Enter Lines To Read : "))
file = open("text.txt","r")
for i in range(n):
    print(file.readline())





# 6 Write a Python program to read a file line by line and store it into a list

fname = 'practice.txt'
def function(fname):
	with open(fname) as file:
		contenct_list = file.readlines()
		print(contenct_list)
function(fname)



#  7  Write a Python program to read a file line by line store it into a variable.

name = 'len.txt'

def longest_word(fname):
	with open(fname,"r") as f:
		words = f.read().spit()

	max_len = len(max(words,key = len))
	return[word for word in words if len(word)==max_len]
	print(longest_word('len.txt'))
	


# 8 Write a Python program to count the number of lines in a text file. 

fname ="practice.txt"

def count(fname):
	with open(fname,'r')as f:
		count1 = len(f.readlines())

		print(count1)
count(fname)



# 9 Write a Python program to count the frequency of words in a file.

file = open('file2.txt','w')

file.write("this is my new file .")
file.close()

file = open('file2.txt','r')
a =file.read()

dict ={}

lines = a.split()

for i in lines:
    keys = dict.keys()

    if  i in keys:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)




# 10 Write a Python program to write a list to a file.

list1 = ["apple","banana","mango","cherry"]
with open('file3.txt','w') as a:
    for i in list1:
        a.write("%s\n" %i)
a.close()

with open('file3.txt',"r") as a:
    print(a.read())




# 11 Write a Python program to copy the contents of a file to another file. 

with open('first.txt','r') as firstfile, open('second.txt','w') as secondfile:
      
    # read content from first file
    for line in firstfile:
               
             # write content to second file
             secondfile.write(line)

# 12 Explain Exception handling? What is an Error in Python?
# In Python, an error is a problem in a program that will stop the execution. On the other hand,
# exceptions are raised when some internal events occur which changes the normal flow of the program
# Python has many built-in exceptions which are raised when your program encounters an error (run-time error).
# You can handle these exceptions using try-except blocks

# try:
    # Your code here
# except ExceptionType:
    # Code to handle the exception





# 13 How many except statements can a try-except block have?/Name Some 
# built-in exception classes: 

# In Python, there has to be at least one except statement in a try-except block. A try statement may have more than one except clause, 
# to specify handlers for different exceptions. At most one handler will be executed



# 14 When will the else part of try-except-else be executed?

# When will the else part of try-except-else be executed? Explanation: The else part is executed when no exception occurs.



# 15 Can one block of except statements handle multiple exception? 
# yes



# 16 What happens when „1‟== 1 is executed?

# When ‘1’ == 1 is executed, it evaluates to False This is because one is a string and the other is an integer1. 
# The comparison is done using operator precedence2. The first (1,) == 1 groups like so: ((1,) == 1), so builds a tuple with a single element from the result of comparing the one-element tuple 1, to the integer 1 for equality.
#  They're not equal,  so you get the 1-tuple False, for a result.


# 17 How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets. 

# An Exception is an Event, which occurs during the execution of the program. It is also known as a run time error. When that error occurs, Python generates an exception during the execution and that can be handled, 
# which avoids your program to interrupt.

def divide(x, y):
    try:
        # Floor Division : Gives only Fractional
        # Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
   
# Look at parameters and note the working of Program
divide(3, 2)
divide(3, 0)

# 18 Write python program that user to enter only odd numbers, else will 
# raise an exception.

# 19 What are oops concepts?
# As the name suggests, Object-Oriented Programming or OOPs refers to languages that use objects in programming. Object-oriented programming aims to implement real-world entities like inheritance, hiding, 
# polymorphism, etc in programming. The main aim of OOP is to bind together the data and 
# the functions that operate on them so that no other part of the code can access this data except that function.

# OOPs Concepts:
# Class
# Objects
# Data Abstraction
# Encapsulation
# Inheritance
# Polymorphism

# 20 How to Define a Class in Python? What Is Self? Give An Example Of A Python Class

# defing the class name office with x property

class office:
	x =" employee"

# 21 Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle 

class Rentangle:
    def area(self,length,width):
        self.length = length
        self.width = width
        area = width * length
        print(area)

length = int(input("write your length :"))
width = int(input("write youe width : "))

b1 = Rentangle()
b1.area(length,width)

# 22 Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle 

class Circle:
    def area(self,radius):
        self.radius = radius
        area = 2* 3.14* (radius*radius)
        print(area)
    def perimeter(self,radius):
        perimeter = 2*3.14*radius
        print(perimeter)


radius = int(input("write your  Circle radius : "))
a = Circle()

a.area(radius)
a.perimeter(radius)


# 23 Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?
# Like any other OOP languages, Python also supports the concept of class inheritance.Inheritance allows us to create a new class from an existing class.
# The new class that is created is known as subclass (child or derived class) and the existing class from which the child class is derived is known as superclass
#  (parent or base class).

# ex:

class Person:
 
    # init method or constructor
    def __init__(self, name):
        self.name = name
 
    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)
 
 
p = Person('Nikhil')
p.say_hi()
