# For Loop

# students =[1,2,3,4,5]

# for a in students:
#     if(a == 10 ):
#         print("found")
#         break
#     print(a)
# else:
#     print("end") 

# 1. Print the elements of the following list using a loop:
# [l, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for a in list1:
#     print(a)

# 2. Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# it is called linear search in coding language means searching in a single line

# tuple1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100,)
# print("Enter Number from this:-\n",tuple1)
# b = int(input("Enter a number: "))
# num =0
# for a in tuple1:
#     if(a == b):
#         print(b,"--> found at",num)
#         break
#     num +=1
#     # else:
#     #     print("Not Found")


#Range() in Loops ----------------------------------------------  

#range(start?,stop,step?)

# for i in range(10):  # range(stop)
#     print(i)

# for i in range(5,10):  # range(start,stop)
#     print(i)

# for i in range(5,10,2):  # range(start,stop,step)
#     print(i)

# 1. Print numbers from 1 to 100.

# for a in range(1,101):
#     print(a)

# 2.Print numbers from 100 to 1.

# for a in range(100,0,-1):
#     print(a)

# 3.Print the multiplication table of a number n.

# print("---------------------------------------------------")
# a = int(input("Enter a Number to Display Table: "))
# print("---------------------------------------------------")
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print("|         Table of",a,"      |")
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# for i in range(1,11):
#     print(a, "*",i,"=",a * i)

# Pass Statement -----------------------------------------------------
# pass is a null statement that does nothing. It is used as a placeholder for future code.

# for i in range(10):
#     pass # for empty loop not in use but exit

# print("End")\



# practic Questions:

# 1.WAP to find the sum of first n numbers. (using while)

# for loop------------------------------
# n=int(input("Enter a Number to do sum of it "))
# sum =0
# for i in range(1, n+1):
#     sum +=i
# print("Total sum =",sum)

# while loop -----------
# n = int(input("Enter a number to do sum of it: "))  # e.g., 5
# sum = 0
# i = 1  # start counter

# while i <= n:
#     sum += i  # add i to sum 
#     i += 1    # increment i

# print("Total sum =", sum)

# 2.WAP to find the factorial of first n numbers. (using for)

# n =int(input("Enter a Number to do Factorical of it "))
# fac =1
# for i in range(1, n+1):
#     fac *=i
# print("Factorial =",fac)
