# While Loop

# print("-------------------------------------------")
# a =5                       # starts with
# while a >=1:                          # condition
#     print(a)                          # Reverse loop
#     a -=1                   #Decrements
# print("-------------------------------------------")
# b = 1                        # starts with
# while b <=5:                          # condition
#     print(b)                           # loop
#     b +=1                #Increments
# print("-------------------------------------------")

# practic questions
# 1.print numbers from 1 to 100

# a = 1
# while a <=100:
#     print(a)
#     a +=1


#2.print numbers from 100 to 1

# a = 100
# while a >=1:
#     print(a)
#     a -=1

# 3.Print the multiplication table of a number n.

# a = 1
# b = int(input("Enter Table number: "))
# print("-------------------------------------------")
# print("This is Table of ",b)
# print("-------------------------------------------")
# while a <=10 :
#     print(b, "*" ,a, "=",a *b )
#     a +=1
# print("-------------------------------------------")


# 4.Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# num =[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# # print(len(num))
# a = 0
# while a< len(num) :
#     print(num[a])
#     a +=1

# 5.Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# a = 0
# x = int(input("Enter a Number: "))
# while a < len(num) :
#     if(num[a] == x):
#         print(x, "is Found at",a)
#     else:
#         print("Finding...")
#     a +=1
    

# Break and Continue in While Loop

#  break → Stop the loop immediately when found     like stop
#  continue → Skip current iteration     like skip


# ------Break---------

# i = 1
# while i<=10:
#     print(i)
#     if(i == 3):
#         break
#     i +=1
# print("End of loop")

# -----Continue-------

# i = 1
# while i <=5:
    
#     if(i == 3):
#         i+=1
#         continue
#     print(i)
#     i +=1

# or  odd even 
# i = 1
# while i <=10:
    
#     if(i %2 ==0):
#         i+=1
#         continue
#     print(i)
#     i +=1