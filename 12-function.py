# Function 

# def function_name(parameters):     # syntax
#     # Code block
#     return result  # (optional)


# def calc_sum(a,b):          # function Definiton      #  1
#     s = a + b                       
#     return s
# print(calc_sum(1,3))          # Function Call
  
# def print_hello():                                      #2
#     print("hello")

# print_hello()

# practic Questions -----------------------------------

# 1. Calcluate Average of 3 Number   

# def calc_avg(a,b,c):
#     sum = a+b+c
#     avg =sum/3
#     print(avg)
#     return avg

# calc_avg(10,10,10)

# 2.WAF to print the length of a list. ( list is the parameter)

# cities =["delhi", "gurgaon", "noida","pune","mumbai", "chennai"]
# heroes =["thor", "ironman", "captain america", "shaktiman"]

# def print_list(list):
#     print(len(list))

# print_list(cities)
# print_list(heroes)

# 3.WAF to print the elements of a list in a single line. ( list is the parameter)

# cities =["delhi", "gurgaon", "noida","pune","mumbai", "chennai"]
# heroes =["thor", "ironman", "captain america", "shaktiman"]

# def print_inline(line):
#     for a in line:
#         print(a, end=" | ")

# print_inline(cities)

# 4.WAF to find the factorial of n. (n is the parameter)

# n = int(input("Enter a number to find factorial: "))

# def factorial(a):
#     fact = 1
#     for f in range(1,a+1):
#         fact *=f
#     print(fact)
# factorial(n)

# 5.WAF to convert USD to INR.

# n = int(input("Enter a number to convert : "))
# def convert(usd):
#     inr = usd * 85
#     print(usd,"USD =",inr,"INR ")

# convert(n)

# 6.WAF take a number as a input if it is odd than return string "odd" or "even"

# num = int(input("Enter a Number: "))

# def check(number):
#     if(number%2 == 0):
#         print(number,"is Even Number")
#     else:
#         print(number,"is Odd Number")

# check(num)


