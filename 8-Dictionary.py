# Dictionaries are used to store data values in key:value pairs
# They are unordered, mutable(changeable) & don't allow duplicate keys

# student = {                 # Dictionay Syntax 
#     "name": "Parth",
#     "age": 18,
#     "grade": "A"
# }

# print(student)     # print Dictionary

# # Accessing items
# print(student["name"])  
# print(student.get("age"))  

# # Modifing Dictionary
# student["grade"] = "A+"     # Update value
# student["course"] = "Python"  # Add new key-value pair
# print(student)     # print Dictionary

# #  Removing Items
# student.pop("age")       # Removes "age" entry
# del student["grade"]     # Deletes "grade" key
# print(student)     # print Dictionary

# Que-1. Store following word meanings in a python dictionary :
# A)table : "a piece of furniture", 'list of facts & figures"
# B)cat : "a small animal"

# Dictionary ={
#     "table" : ["a piece of furniture","list of facts and figures"],
#     "cat" : "a samll animal"
# }

# print(Dictionary)

# q.2 WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

# marks = {}

# a = int(input("Enter math marks : "))
# b = int(input("Enter science marks : "))
# c = int(input("Enter english marks : "))

# marks.update({"Math" : a ,"Science" : b, "English" : c})
# print(marks)

