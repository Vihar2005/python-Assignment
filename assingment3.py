# B1 What is File function in python?what is keywords to create and write file.

Open the File: You use the open() function to open a file. It takes two arguments: the file name and the mode in which you want to open the file
(e.g., "r" for read, "w" for write, "a" for append, "b" for binary mode, etc.).

Write to the File: If you want to write to the file,
you can use methods like write() to add content to the file.

Close the File: After you're done with the file, it's essential to close it using the close() method.
This ensures that any changes are saved and that system resources are released.


# B2 Write a Python program to read an entire text file

file_name = "example.txt"
try:
    with open(file_name, "r") as file:
        file_content = file.read()
        print(file_content)

except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")

except PermissionError:
    print(f"You don't have permission to read '{file_name}'.")

except Exception as e:
    print(f"An error occurred: {e}")


# B3 Write a Python program to append text to a file and display the text. 


file_name = "example.txt"
try:
    with open(file_name, "a") as file:
        text_to_append = input("Enter text to append to the file: ")
        file.write(text_to_append + "\n")
    with open(file_name, "r") as file:
        file_content = file.read()
        print("Updated File Content:")
        print(file_content)

except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")

except PermissionError:
    print(f"You don't have permission to write to '{file_name}'.")

except Exception as e:
    print(f"An error occurred: {e}")


# B4 Write a Python program to read first n lines of a file

file_name = "example.txt"
try:
    with open(file_name, "r") as file:
        n = int(input("Enter the number of lines to read: "))
        line_count = 0
        for line in file:
            print(line, end="")
            line_count += 1
            if line_count >= n:
                break

except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")

except PermissionError:
    print(f"You don't have permission to read '{file_name}'.")

except Exception as e:
    print(f"An error occurred: {e}")


#5 Write a Python program to read last n lines of a file

from collections import deque

file_name = "example.txt"
try:
    with open(file_name, "r") as file:
        n = int(input("Enter the number of lines to read: "))
        last_lines = deque(maxlen=n)
        for line in file:
            last_lines.append(line)
        print("Last", min(n, len(last_lines)), "lines of the file:")
        for line in last_lines:
            print(line, end="")

except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")

except PermissionError:
    print(f"You don't have permission to read '{file_name}'.")

except Exception as e:
    print(f"An error occurred: {e}")



#  I1 Write a Python program to read a file line by line and store it into a list

file_name = "example.txt"
try:
    with open(file_name, "r") as file:
        lines_list = []
        for line in file:
            lines_list.append(line.strip())
        print("Contents of the file stored in a list:")
        for line in lines_list:
            print(line)

except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")
except PermissionError:
    print(f"You don't have permission to read '{file_name}'.")
except Exception as e:
    print(f"An error occurred: {e}")



# I2 Write a Python program to read a file line by line store it into a variable. 


file_name = "example.txt"
try:
    with open(file_name, "r") as file:
        file_content = ""
        for line in file:
            file_content += line
        print("File content stored in a variable:")
        print(file_content)

except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")

except PermissionError:
    print(f"You don't have permission to read '{file_name}'.")

except Exception as e:
    print(f"An error occurred: {e}")


# I3 Write a python program to find the longest words

text = "This is a sample sentence to find the longest words in the text."
words = text.split()

longest_words = []
max_length = 0

for word in words:
    word = word.strip(".,!?")
    word_length = len(word)
    
    if word_length > max_length:
        max_length = word_length
        longest_words = [word]
    elif word_length == max_length:
        longest_words.append(word)

print("Longest words in the text:")
for word in longest_words:
    print(word)


# I4 Write a Python program to count the number of lines in a text file. 


file_name = "example.txt"
try:
    with open(file_name, "r") as file:
        line_count = 0
        for line in file:
            line_count += 1
        print(f"Total number of lines in '{file_name}': {line_count}")

except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")

except PermissionError:
    print(f"You don't have permission to read '{file_name}'.")

except Exception as e:
    print(f"An error occurred: {e}")


# I5 Write a Python program to count the frequency of words in a file


file_name = "example.txt"
try:
    with open(file_name, "r") as file:
        word_count = {}
        for line in file:
            words = line.split()
            for word in words:
                word = word.strip(".,!?").lower()
                if word:
                    word_count[word] = word_count.get(word, 0) + 1
        print("Word frequencies in the file:")
        for word, count in word_count.items():
            print(f"{word}: {count}")

except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")

except PermissionError:
    print(f"You don't have permission to read '{file_name}'.")

except Exception as e:
    print(f"An error occurred: {e}")


# I6 Write a Python program to write a list to a file.

my_list = ["apple", "banana", "cherry", "date"]
file_name = "my_list.txt"
try:
    with open(file_name, "w") as file:
        for item in my_list:
            file.write(item + "\n")
    print(f"The list has been written to '{file_name}'.")

except PermissionError:
    print(f"You don't have permission to write to '{file_name}'.")

except Exception as e:
    print(f"An error occurred: {e}")




# A1 Write a Python program to read a random line from a file. 

import random

file_name = "example.txt"
try:
    with open(file_name, "r") as file:
        total_lines = sum(1 for _ in file)
        random_line_number = random.randint(1, total_lines)
        file.seek(0)

        for line_number, line in enumerate(file, start=1):

            if line_number == random_line_number:
                print(f"Random Line {random_line_number}: {line.strip()}")
                break

except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")

except PermissionError:
    print(f"You don't have permission to read '{file_name}'.")

except Exception as e:
    print(f"An error occurred: {e}")


# A2 Write a Python program to assess if a file is closed or not

file_name = "example.txt"
try:
    file = open(file_name, "r")
    if file.closed:
        print(f"The file '{file_name}' is closed.")
    else:
        print(f"The file '{file_name}' is open.")
    file.close()

    if file.closed:
        print(f"The file '{file_name}' is closed.")
    else:
        print(f"The file '{file_name}' is still open.")

except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")

except PermissionError:
    print(f"You don't have permission to open '{file_name}'.")

except Exception as e:
    print(f"An error occurred: {e}")


# A3 Write a Python program to remove newline characters from a file.

file_name = "example.txt"
try:
    with open(file_name, "r") as file:
        lines = file.readlines()

    with open(file_name, "w") as file:
        for line in lines:
            line_without_newline = line.strip() 
            file.write(line_without_newline)
    print(f"Newline characters have been removed from '{file_name}'.")

except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")

except PermissionError:
    print(f"You don't have permission to modify '{file_name}'.")

except Exception as e:
    print(f"An error occurred: {e}")



# B1 Explain Exception handling?What is an Error in Python?

Exception handling is a critical concept in programming, including in Python. It refers to the process of managing and responding to unexpected
or exceptional events that can occur during the execution of a program. These exceptional events, known as exceptions, can disrupt the normal flow of a program.
Exception handling allows you to gracefully handle these situations, preventing your program from crashing and providing a way to respond to errors.


# B2 How many except statements can a try-except block have? 

 a try-except block can have one or more except statements to handle different types of exceptions.
  This allows you to specify different handling logic for various types of exceptions that may occur within the try block.
      

# B3 When will the else part of try-except-else be executed?

you can use a try-except-else block to specify code that should be executed when no exceptions are raised within the try block.
 The else block will run if and only if the code in the try block executes successfully without any exceptions.


# B4 Can one block of except statements handle multiple exception? 

one except block can handle multiple exceptions by specifying those exceptions as a tuple in the except statement.
This allows you to provide the same handling logic for multiple exception types in a single except block, reducing code duplication.
    

# B5 When is the finally block executed?

After the try block: The finally block is executed after the code in the try block has executed, regardless of whether an exception was raised or not.
 This means that even if an exception occurs and is caught by an except block, the finally block will still execute.


# B6 What happens when ‘1’ == 1 is executed?

When you execute the expression '1' == 1 in Python, you are comparing two values: a string containing the character '1' and an integer with the numeric value 1


# B7 write python program that user to enter only odd numbers, else will raise an exception.

try:
    number = int(input("Enter an odd number: "))
    if number % 2 == 0:
        raise ValueError("You entered an even number.")
except ValueError as e:
    print(f"Error: {e}")
else:
    print(f"You entered an odd number: {number}")



# I1 write program for Catching Specific Exceptions in Python

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
except ValueError as ve:
    print(f"ValueError: {ve} - Please enter valid numbers.")
except ZeroDivisionError as zde:
    print(f"ZeroDivisionError: {zde} - Division by zero is not allowed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"Result of the division is: {result}")


# I2 write python program for file operations to makes sure the file is closed even if an exception occurs.

try:
    # Open a file for writing
    file_name = "example.txt"
    file = open(file_name, "w")

    # Perform file operations
    file.write("Hello, World!")

    # Simulate an exception (e.g., division by zero)
    result = 10 / 0

except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    # Ensure the file is closed, regardless of exceptions
    if 'file' in locals():
        file.close()

print(f"File '{file_name}' is closed: {file.closed}")


# I3 Explain Python Errors and Built-in Exceptions with coding snippets.

errors are issues that prevent a program from running successfully. Python provides a mechanism to handle these errors using exceptions.
Exceptions are objects that represent errors and exceptional situations that can occur during program execution. When an error occurs,
an exception is raised, and you can use try, except, else, and finally blocks to handle these exceptions gracefully.


# A1 Explain .User-Defined Exception in Python

you can create your own custom exceptions, known as user-defined exceptions, to handle specific error scenarios or conditions in your code. User-defined exceptions allow you to define custom error classes
that inherit from the base Exception class or one of its subclasses. By doing this, you can raise and catch your custom exceptions just like built-in exceptions.


# A2 write .program that will ask the user to enter a number until they guess a stored number correctly.

import random

target_number = random.randint(1, 100)
user_guess = None
attempts = 0
while user_guess != target_number:
    try:
        user_input = input("Guess the number (between 1 and 100): ")
        user_guess = int(user_input)
        attempts += 1
        if user_guess < target_number:
            print("Too low! Try again.")
        elif user_guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


# A3 What is Assertions in Python? Write function that converts a temperature from degrees Kelvin to degrees Fahrenheit

assertions are a way to include debugging and error-checking statements in your code. An assertion is a statement that checks whether a given condition is True.
If the condition is False, an AssertionError exception is raised. Assertions are often used during development and testing to catch programming errors early.
They provide a way to express expectations about the state of your code and are typically disabled in production code for performance reasons.


# A4 Write program that except Clause with No Exceptions

try:
    result = 10 / 2  # No exceptions are raised here
except:
    print("An exception occurred or didn't occur.")
print("Program continues after the try-except block.")


# A5 What is Argument of an Exception?Explain with coding snippets

an argument of an exception, often referred to as the exception message, is a string or another object associated
with an exception instance that provides additional information about the error that occurred.It's a way to
 communicate details about the exception to help diagnose and debug issues in your code.



# B1 what are oops concepts?is multiple inheritance supported in java



# B2 How To Define a Class in Python?What Is Self?Give An Example Of A Python Class 

 you can define a class using the class keyword. A class is a blueprint for creating objects, and it defines the attributes (data members) and methods
(functions) that the objects of the class will have. The self keyword is a convention in Python used as the first parameter in methods within a class.
  It refers to the instance of the class itself, allowing you to access and modify its attributes and methods.


# B3 Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        area = self.length * self.width
        return area
my_rectangle = Rectangle(5, 8)
area = my_rectangle.compute_area()
print(f"The area of the rectangle is: {area}")


# B4 Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        area = math.pi * self.radius**2
        return area

    def compute_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter
my_circle = Circle(5)
area = my_circle.compute_area()
perimeter = my_circle.compute_perimeter()

print(f"The area of the circle is: {area}")
print(f"The perimeter of the circle is: {perimeter}")


# B6 Explain Inheritance in Python with an example.?What Is init ? Or What Is A Constructor In Python?

Inheritance is one of the fundamental concepts of object-oriented programming (OOP) in Python and many other programming languages.
Inheritance allows you to create a new class that inherits properties and behaviors (attributes and methods) from an existing class.
The existing class is referred to as the "parent" or "base" class, and the new class is known as the "child" or "derived" class.
Inheritance promotes code reuse and allows you to create a hierarchy of classes with shared characteristics.


# B7 What is Instantiation in terms of OOP terminology?

In object-oriented programming (OOP) terminology, instantiation refers to the process of creating an instance or an object of a class.
 An instance is a concrete, individual, and distinct entity created from a class, which serves as a blueprint or template.
 When you instantiate a class, you are essentially creating a unique object with its own set of attributes and methods defined by the class.



# B8 What is used To check whether an object o is an instance of class A?

you can use the isinstance() function to check whether an object is an instance of a particular class or a subclass of that class. The isinstance()
 function takes two arguments: the object you want to check and the class (or a tuple of classes) you want to check against.
 It returns True if the object is an instance of the specified class or any of its subclasses; otherwise, it returns False.


# B9 What relationship is appropriate for Course and Faculty?

 the appropriate relationship between the Course and Faculty classes would typically be an association or a many-to-many relationship.
 This means that multiple courses can be associated with multiple faculty members, and vice versa. This relationship can be
represented using various approaches, including lists, sets, or databases. Here, I'll provide a simple example using lists.


# I1 Which function overloads the + operator?Which operator is overloaded by ___invert___ ()? 

the + operator is overloaded by the __add__() method, which allows you to define custom behavior for the addition operation when applied to objects of a class.
 By implementing the __add__() method, you can specify how instances of your class should behave when the + operator is used with them.


# I2 Which function overloads the >> operator?

the >> operator is not directly overloaded with a specific method like some other operators (+, -, *, ==, etc.). Instead, the behavior of the >> operator is
 associated with the __rshift__() method in the context of right shifting.


# I3 Create a class called Numbers, which has a single class attribute called MULTIPLIER, and a constructor which takes the parameters x and y (these should all be numbers).

class Numbers:
    MULTIPLIER = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y
num_instance = Numbers(5, 10)
print(f"x: {num_instance.x}")
print(f"y: {num_instance.y}")
print(f"MULTIPLIER: {Numbers.MULTIPLIER}")



# A1 Write a Python class to implement pow(x, n)

class PowerCalculator:
    def calculate_power(self, x, n):
        return x ** n
calculator = PowerCalculator()
result = calculator.calculate_power(2, 3)
print(f"2^3 = {result}")
