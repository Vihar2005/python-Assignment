# i1 Write a Python program to access a function inside a function.

def outer_function():
    def inner_function():
        print("This is the inner function!")

    print("Calling the inner function from the outer function:")

    Calling the inner function from the outer function:
    This is the inner function!

# i2 Write a Python program to detect the number of local variables declared in a function. 

def my_function():
    var1 = 10
    var2 = 'hello'
    var3 = [1, 2, 3]

    local_variables = locals()
    num_local_variables = len(local_variables)

    return num_local_variables
    num_locals = my_function()
    print(f"The number of local variables in the function is: {num_locals}")


# i3 What is map function in Python?

In Python, the map() function is a built-in higher-order function that applies a specified
  function to all items in an iterable (e.g., a list, tuple, or set) and returns an iterator
 that yields the results. It takes two arguments: the function to be applied and the iterable.


# i4 Does Python Have A Main() Method?

in Python, unlike some other programming languages like Java or C++, there is no explicit main() method. However,
  Python uses a special variable called __name__ to determine the entry point of the program.


# i5 What Does The *Args Do In Python?What Does The **Kwargs Do In Python?

In Python, *args and **kwargs are special syntax used in function definitions to allow functions to accept
  a variable number of arguments. They are often used when you're unsure about the number of arguments that a function might receive.


# i6 What Does The Name Do In Python?What Is The Purpose Of “End” In Python? 

#__name__ in Python:
__name__ is a built-in attribute in Python that is automatically created for every module and script.
It is a string that holds the name of the module or script.The value of __name__ depends on how the module or script is being used:

#end in Python:
end is an optional parameter in the print() function in Python. It specifies what to print at the end of the printed output. By default,
the end parameter is set to '\n', which means the print() function adds a newline character after printing the given content.


# i7 What Does The Len() Function Do In Python? What Does The Ord() Function Do In Python?

#len() function in Python:
The len() function is a built-in function in Python that is used to determine the length of an object. It works with various data types, including strings, lists, tuples, sets, and dictionaries.
The purpose of the len() function is to return the number of elements in the given object.

#ord() function in Python:
The ord() function is another built-in function in Python that takes a single character (a string of length 1) as an argument and returns its Unicode code point (integer representation).
It essentially converts the given character to its corresponding Unicode integer value.


# -----------------module 4-------------------

# b1 How can you pick a random item from a list or tuple?

You can pick a random item from a list or tuple in Python using the random module. The random module provides a function called choice() that selects a random element from a sequence
(e.g., list, tuple) with uniform probability.


# b2 How can you pick a random item from a range?

To pick a random item from a range in Python, you can use the random.choice() function along with the range() function. The range() function generates a sequence of numbers within the specified range,
 and then you can use random.choice() to pick a random element from that sequence.


# b3 How can you get a random number in python?

You can get a random number in Python by using the random module, which provides several functions for generating random values. 


# b4 How will you set the starting value in generating random numbers?

In Python, you can set the starting value for generating random numbers by using the random.seed() function from the random module.
   The random.seed() function initializes the random number generator with a specific seed value, which ensures that the sequence of
    random numbers generated remains the same across different runs of the program, given the same seed value.


# b5 How will you randomizes the items of a list in place?

To randomize the items of a list in place, you can use the random.shuffle() function from the random module. The random.shuffle()
function shuffles the elements of a list randomly, modifying the list in place without creating a new list.

# i1 Write a Python program to read a random line from a file. 

To read a random line from a file in Python, you can use the random module along with the linecache module.
 The random module will help you generate a random line number, and the linecache module will allow you to
 access a specific line from the file efficiently.


# i2 Write a Python program to convert degree to radian.

import math

def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)
    return radians

# Example usage:
degrees = 45
radians = degrees_to_radians(degrees)
print(f"{degrees} degrees is equal to {radians:.2f} radians.")


# i3 Write a Python program to calculate the area of a trapezoid 

def trapezoid_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area
base1 = float(input("Enter the length of the first base: "))
base2 = float(input("Enter the length of the second base: "))
height = float(input("Enter the height: "))

area = trapezoid_area(base1, base2, height)
print(f"The area of the trapezoid is: {area}")


# i4 Write a Python program to calculate the area of a parallelogram.

def parallelogram_area(base, height):
    area = base * height
    return area

base_length = float(input("Enter the length of the base: "))
height = float(input("Enter the height: "))

area = parallelogram_area(base_length, height)
print(f"The area of the parallelogram is: {area}")


# i5 Write a Python program to calculate surface volume and area of a cylinder

import math

def cylinder_surface_area(radius, height):
    area = 2 * math.pi * radius * (radius + height)
    return area

def cylinder_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

surface_area = cylinder_surface_area(radius, height)
volume = cylinder_volume(radius, height)

print(f"The surface area of the cylinder is: {surface_area:.2f}")
print(f"The volume of the cylinder is: {volume:.2f}")


# i6 Write a Python program to returns sum of all divisors of a number 

def sum_of_divisors(number):
    divisor_sum = 0

    for i in range(1, number + 1):
        if number % i == 0:
            divisor_sum += i

    return divisor_sum

number = int(input("Enter a number: "))

result = sum_of_divisors(number)
print(f"The sum of divisors of {number} is: {result}")


# i7 Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

def find_max_min(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    return maximum, minimum
 
input_numbers = input("Enter decimal numbers separated by spaces: ")
numbers_list = [float(num) for num in input_numbers.split()]
max_number, min_number = find_max_min(numbers_list)

print(f"The maximum number is: {max_number}")
print(f"The minimum number is: {min_number}")


# a1 Write a Python program to find the sum of the following decimal numbers and display the numbers in sorted order

def main():
    
    input_numbers = input("Enter decimal numbers separated by spaces: ")
    numbers_list = [float(num) for num in input_numbers.split()]
    total_sum = sum(numbers_list)
    sorted_numbers = sorted(numbers_list)

    print(f"The sum of the numbers is: {total_sum}")
    print("Numbers in sorted order:")
    for number in sorted_numbers:
        print(number)

if __name__ == "__main__":
    main()


# a2 Write a Python program to get the square root and exponential of a given decimal number.

import math

def square_root_and_exponential(number):
    square_root = math.sqrt(number)
    exponential = math.exp(number)
    return square_root, exponential

decimal_number = float(input("Enter a decimal number: "))
sqrt, exp = square_root_and_exponential(decimal_number)

print(f"The square root of {decimal_number} is: {sqrt:.4f}")
print(f"The exponential of {decimal_number} is: {exp:.4f}")


# a3 Write a Python program to add, subtract, multiply and divide two fractions. 

from fractions import Fraction

def perform_operations(fraction1, fraction2):
    # Addition
    addition_result = fraction1 + fraction2

    # Subtraction
    subtraction_result = fraction1 - fraction2

    # Multiplication
    multiplication_result = fraction1 * fraction2

    # Division
    division_result = fraction1 / fraction2

    return addition_result, subtraction_result, multiplication_result, division_result

fraction_str1 = input("Enter the first fraction (in the format a/b): ")
fraction_str2 = input("Enter the second fraction (in the format a/b): ")

fraction1 = Fraction(fraction_str1)
fraction2 = Fraction(fraction_str2)

addition, subtraction, multiplication, division = perform_operations(fraction1, fraction2)


