#B1.What is Python ,Name some of the features of Python.

-> Python is a popular high-level programming language known for its simplicity and
readability.It was created by Guido van Rossum and first released in 1991.Here are
some of the features of Python:

#B2.Is python the right choice for Web based Programming? 

-> Yes, Python is a great choice for web-based programming. Python provides several
frameworks and libraries that make web development efficient and straightforward.

#B3.Why was the language called as Python?

-> The programming language Python was named after the British comedy group Monty Python.
Guido van Rossum, the creator of Python, was a fan of the group and wanted to choose a fun
and memorable name for his new programming language. He decided to name it Python in honor
of Monty Python's Flying Circus, a popular comedy show in the 1970s.

#B4.Write a Python program to check if a number is positive, negative or zero.

-> a = int(input())

if a < 0:
    print(a, " : is Negative number")
elif a == 0:
    print(a, " : 0")
else:
    print(a, " is  Positive number")

#B5.What is the language from which Python has got its features or derived its features? 

-> C: Python's syntax and design are influenced by the C programming language.
Many C programming constructs, such as loops, conditionals, and functions, are similar in Python.

#B6.Write a Python program to check if variable is of integer or string.

-> # int

a=1020304050601233
print("A : ",a)
print(type(a))

# string

a='10203040.50601233'
print("A : ",a)
print(type(a))


#B7.Does python support switch or case statement in Python?



#B8.How Python is interpreted?

-> Python is an interpreted language, which means that it is executed line by line at runtime
without the need for a separate compilation step. 

1:Source Code: Python programs are written in human-readable text format called source code.
A Python source code file typically has a .py extension.

2:Dynamic Typing and Memory Management: Python is dynamically typed, so variable types are
determined at runtime. During execution, the interpreter handles memory management, including
memory allocation and deallocation. Python utilizes a garbage collector to automatically
deallocate memory for objects that are no longer in use.


#B9.Write a Python program to get the Factorial number of given number.

-> num = int(input())
factorial = 1
if num < 0:
    print("we can't find factorial")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(factorial)


#B10.Write a Python program to get the Fibonacci series of given range.

->inp = int(input("fibonacci :"))
n1, n2 = 0, 1
count = 0
if inp <= 0:
    print('please enter positive number')
elif inp == 1:
    print(n1)
    print(inp)
else:
    print("fibonacci")
    while count < inp:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

#B11.How memory is managed in Python?

->Memory management in Python is handled automatically by the Python interpreter through a combination
of techniques, including reference counting and a garbage collector.

#B12.What is namespace in Python?

->In Python, a namespace is a container that holds a collection of names (variables, functions,
classes, etc.) and maps them to their corresponding objects. It provides a way to organize and
differentiate between different names used in a program to avoid naming conflicts.

Namespaces play a crucial role in Python's scoping and name resolution rules. They help in
determining the scope and accessibility of names within a program. Each namespace is unique
and independent, and different namespaces can coexist within the same program.

#B13.What is the purpose continue statement in python?

->The continue keyword is used to end the current iteration in a for loop (or a while loop),
 and continues to the next iteration.

#I1. Write python program that swap two number with temp variable and without temp variable.

->x = int(input("enter the value of x :"))
y = int(input('enter the value of y:'))

temp = x
x = y
y = temp
print('not x value is :', x)
print('not y value is :', y)

# without temp variable

x = 20
y = 30

print("before swaping numbers: ", x, " ", y)
x, y = y, x
print("after swapig numbera:", x, " ", y)


#I2. Write a Python program to find whether a given number is even or odd, print out an appropriate
#message to the user.

->x = int(input())


def evenodd(x):
    if x % 2 == 0:
        print("your value is even number")
        else:
        if x % 2 != 0:
            print("your value is even")


print(evenodd(x))


#I3.Write a Python program that compute the area of following
# 1) Triangle (accepts base and height)2) Circle (accept radius).

->import math

def triangle(base, height):
    area = 0.5 * base * height
    return area

def circle(radius):
    area = math.pi * radius ** 2
    return area

# Triangle
base = float(input("Enter triangle base: "))
height = float(input("Enter triangle height: "))
triangle_area = triangle(base, height)
print("The area of the triangle is:", triangle_area)

# Circle
radius = float(input("Enter circle radius: "))
circle_area = circle(radius)
print("The area of the circle is:", circle_area)


#I4.Write a Python program to test whether a passed letter is a vowel or not.

->x = input('find ,the letter is vowel or not   :')
vowel = 'aeiouAEIOU'
if x in vowel:
    print('yes Typed letter is vowel')
else:
    print('it is not vowel')


#I5.Write a Python program to compute the value of a specified principal
# amount, rate of interest, and a number of years.

->def interest(principal, rate, years):
    interest = principal * rate * years
    total_value = principal + interest
    return total_value

principal_amount = int(input("Enter the principal amount: "))
interest_rate = int(input("Enter the rate of interest (in decimal form): "))
num_of_years = int(input("Enter the number of years: "))

result = interest(principal_amount, interest_rate, num_of_years)
print("The value after", num_of_years, "years will be:", result)


#I6.What are the tools that help to find bugs or perform static analysis?

->


#I7.What are Python decorators?

->In Python, decorators are a way to modify or enhance the behavior of functions or classes
without directly changing their source code. Decorators allow you to wrap a function or a class
with another function, called a decorator function, which can add functionality, modify arguments
or return values, or perform other operations.


#I8.What is PEP 8? 

->PEP 8 is the official style guide for Python code. "PEP" stands for Python Enhancement Proposal,
and PEP 8 specifically focuses on the guidelines and recommendations for writing clean, readable,
and consistent Python code.

#A1.Write a Python program to sort three integers without using conditional statements and loops.

->


#A2.- Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

->


#A3. Write a Python program to sum of three given integers.However, if two values are equal sum will be zero

->x, y, z = int(input()), int(input()), int(input())

if x == y or y == z or z == x:
    plus = 0
    print(plus)
else:
    plus = x + y + z
    print('sum: ', plus)


#A4. Write a Python program that will return true if the two given integer
# values are equal or their sum or difference is 5.

->x = int(input())
y = int(input())

plus = x + y
dif = x - y


def function(x, y):
    if x == y or plus == 5 or dif == 5:
        print(True)


function(x, y)

#A5.Write a python program to sum of the first n positive integers.

->n = int((input()))

s = (n + 1) * n / 2
print(s)


#B1.Write a Python program to calculate the length of a string.

->string = input()
a = len(string)
print('the length of this string is : ', a)


#B2.Write a Python program to count the number of characters (character frequency)in a string.

->str = input()


def function(str):
    dict = {}
    for n in str:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    print(dict)


function(str)


#B3.What are negative indexes and why are they used?

->Negative indices are powers(also called exponents) with a minus sign in front of them.used
to in Python to begin slicing from the end of the string i.e. the last.


#B4.Explain split(), sub(), subn() methods of “re” module in Python.

->



#B5.How do you perform pattern matching in Python? Explain.

->


#B6.Write a Python program to count occurrences of a substring in a string.

->string = input()
sub = input()
count = 0
for i in range(0, len(string)):
    stat = i
    end = i + len(sub)
    count = count + string.count(sub, stat, end)
print(count)


#B7.Write a Python program to count the occurrences of each word in a given sentence.

->sentence = input('type your sentence:')
word = input()
a = sentence.split(' ')
count = 0
for i in range(0,len(a)):
    if word == a[i]:
        count += 1
    else:
        pass
print(count)


#I1.Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.

->a = 'xyz'
b = 'abc'
print(a, ' ', b)


def function(a, b):
    new_a = a[:2] + b[2:]
    new_b = b[:2] + a[2:]
    print(new_a, ' ', new_b)


function(a, b)


#I2.Write a Python program to add 'ing' at the end of a given string
# (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead
# If the string length of the given string is less than 3, leave it unchanged.

->a = input()
if len(a) >= 3:
    print(a + "ing")
    if a[-1:-3] == 'ing':
        print(a, 'ly')
else:
    print(a)


#I3.Write a Python program to find the first appearance of the substring 'not'
# and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.

->def not_poor(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')

    if spoor > snot and snot > 0 and spoor > 0:
        str1 = str1.replace(str1[snot:(spoor + 4)], 'good')
        return str1
    else:
        return str1


print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))


#I4.Write a Python function that takes a list of words and returns the length of the longest one.

->def longest(a):
    max1 = len(a[0])
    temp = a[0]
    for i in a:
        if len(i) > max1:
            max1 = len(i)
            temp = i
    print('longest number is :', temp, 'the length of this word is ', max1)


longest(a)


#I5.Write a Python function to reverses a string if it's length is a multiple of 4

->a = input()


def reverse(a):
    if len(a) % 4 == 0:
        print(a[::-1])
    else:
        pass


reverse(a)


#A1.Write a Python program to get a string made of the first 2 and the last 2 chars
# from a given a string. If the string length is less than 2, return instead of the empty string.
# Go to the editor
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

->def string(string):
    if len(string) < 2:
        return ""
    else:
        return string[:2] + string[-2:]

sample_string_1 = 'w3resource'
result_1 = string(sample_string_1)
print(result_1)

sample_string_2 = 'w3'
result_2 = string(sample_string_2)
print(result_2) 

sample_string_3 = ' w'
result_3 = string(sample_string_3)
print(result_3)

#A2.Write a Python program to get a string from a given string where all occurrences
# of its first char have been changed to '$', except the first char itself.

->


#A3.Write a Python function to insert a string in the middle of a string.

-> test_str = 'car is for race'

 print('the original sring ' + str(test_str))
 mid_str = 'good'

 temp = test_str.split()
 mid_pos = len(temp) // 2

 res = temp[:mid_pos] + [mid_str] + temp[mid_pos:]
 res = ' '.join(res)
 print('formated: ', res)
