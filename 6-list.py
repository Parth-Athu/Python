# A list is a built-in data structure in Python that allows you to store multiple items in a single variable.
# list = mutable (changable)

# list =[1,3,2]   # list template -- list = []
# print("simple: ",list)

# list.append(4)    #add one element at the end 
# print("Append: ",list)

# list.sort()   # sort in ascending order 
# print("sort",list)

# list.sort(reverse=True)  # sort in descending order
# print("sort reverse True: ",list)

# list.sort(reverse=False)  # sort in descending order for normal
# print("sort reverse False: ",list)

# list.reverse() # reverses list
# print("Reverse: ",list)

# list.insert(1,5)
# print("Insert: ",list)

# list.remove(5)     # remove  selected  element
# print("Remove: ",list)

# list.pop(2) # remove  a element
# print("pop: ",list)


# # 1) WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

# print(" ~~ List Storing ~~")

# print("Enter Three Movie Name:- ")

# movie = []     #Empty list 
# mov = input("Enter 1st Movie Name: ")
# movie.append(mov)
# mov = input("Enter 2nd Movie Name: ")
# movie.append(mov)
# mov = input("Enter 3rd Movie Name: ")
# movie.append(mov)

# print(movie)


# 2. WAP to check if a list contains a palindrome of elements. 
# (Hint: use copy( ) method)

# list1 = [1, 2, 1]               # Original list

# copy_list = list1.copy()        # Creates a copy so we don't change the original
# copy_list.reverse()             # Reverses the copied list

# if copy_list == list1:          # Compares original and reversed list
#     print("Palindrome")
# else:
#     print("Not palindrome")

# 3.Store the students Grade values in a list & sort them from "A" to "D".

# grades = ["C", "D", "A", "A", "B", "B", "A"]   # Same grades, but in a list

# grades.sort()                                 # Sorts the list in alphabetical order
# print("Sorted grades:", grades)
