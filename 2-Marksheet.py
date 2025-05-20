print("~~~~~~~~~~~~~~~~~~~~~~")
print("  ~~ Marksheet ~~  ")
print("~~~~~~~~~~~~~~~~~~~~~~")
name = input("Enter Your name: ")
Roll_no = input("Enter Your Roll.no: ")
print("Enter Marks according to Suject(out of 100):-")
java = int(input("Enter java Marks: "))
python = int(input("Enter Python marks: "))
html =int(input("Enter HTML marks: "))

print("-------------------------------------------")
print("Name: ", name)
print("Roll.no: ",Roll_no)
print("-------------------------------------------")
print("Marks:-")
print("java:   ",java)
print("python: ",python)
print("HTML:   ",html)

total = java + python + html
percentage = total/3

print("-------------------------------------------")
print("Total: ", total ,"out of 300")
print("-------------------------------------------")
# print("Percentage: ",percentage)
print("Percentage: ", round(percentage, 2), "%")
print("-------------------------------------------")

if( percentage >= 85):
    print("Grade: A+")
elif(percentage <=84 and percentage >=75):
    print("Grade: A")
elif(percentage <=74 and percentage >=60):
    print("Grade: B+")
elif(percentage <=59 and percentage >=50):
    print("Grade: B")
elif(percentage <=49 and percentage >=35):
    print("Grade: C+")
else:
    print("Grade: Fail")

print("-------------------------------------------")