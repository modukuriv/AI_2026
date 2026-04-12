#Let's learn numbers 
#We use numbers in our daily to count, measure and perform calculations.
#In Python, we can use numbers to perform various operations such as addition, subtraction, multiplication, and division.
#So there are two types of numbers in Python: integers and floating-point numbers.

#1. Integers (int) - These are whole numbers without a decimal point. For example: 1, 2, 3, -4, 0, etc.
addition_result = 2 + 2 #Output - 4 (Addition)
print(addition_result)

subtraction_result = 10 - 5 #Output - 5 (Subtraction)
print(subtraction_result)  

multiplication_result = 4 * 3 #Output - 12 (Multiplication)
print(multiplication_result)

division_result = 20 / 4 #Output - 5.0 (Division)
print(division_result) 
#In maths, we have a concept called order of operations,BODMAS (Brackets, Orders, Division and Multiplication, Addition and Subtraction) which tells us the order in which we should perform operations in a mathematical expression.
#In Python, we follow the same order of operations as in mathematics.
#For example:
result = 2 + 3 * 4 #Output - 14 (Multiplication is performed before addition)
print(result)

result = (2 + 3) * 4 #Output - 20 (Brackets are performed first)
print(result)

#2. Let's learn second type of numbers - Floating-point numbers (float) - These are numbers that have a decimal point. For example: 3.14, -0.5, 0.0, etc.
pi = 3.14
print(pi) #Output - 3.14

temperature = -0.5
print(temperature) #Output - -0.5

#Quick intro on Types - In programing, every value has a type 
#The type of a value determines what kind of operations we can perform on it and how it is stored in memory.
#In Python, we can check the type of a value using the type() function.
print(type(pi)) #Output - <class 'float'>
print(type(temperature)) #Output - <class 'float'>
print(type(addition_result)) #Output - <class 'int'>
print(type(subtraction_result)) #Output - <class 'int'>
print(type(multiplication_result)) #Output - <class 'int'>
print(type(division_result)) #Output - <class 'float'>

#so sometimes we may see type errors when we peform operations on values of different types. 
# For example, if we try to add an integer and a string, we will get a type error.

student_id = 12345
student_name = "Alex Robinson"

#Uncomment the below two lines to see the type error

#student_details = student_id + student_name #Output - TypeError: unsupported operand type(s) for +: 'int' and 'str'
#print(student_details)

#So we have tell Python to convert the integer to a string before we can concatenate it with the student_name string. 
# We can do this using the str() function. - and same function we used in day01_variables.py to convert the integer to a string before concatenating it with another string.
#This process is called type conversion or type casting.

student_details = str(student_id) + " " + student_name
print(student_details) #Output - 12345 Alex Robinson


#practice problems:

a = 4 + 4
print(a) #Output - 8

b = 4 * 2 
print(b) #Output - 8

c = 18 - 10
print(c) #Output - 8

d = 16 /2 
print(d) #Output - 8.0

#by the this time you might nnotices # and ''' in the code, these are called comments
# they are used to explain the code and make it more readable.
# for single line comments we use # and 
# for multi-line comments we use ''' or """


