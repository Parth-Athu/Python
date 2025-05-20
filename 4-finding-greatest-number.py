print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" ~~ Finding Greatest Number ~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("Enter Three Number:-")
a= int(input("Enter a: "))
b= int(input("Enter b: "))
c= int(input("Enter c: "))

print("-------------------------------------------------")
print("You entered: a =", a, ", b =", b, ", c =", c)
print("-------------------------------------------------")

if(a>b and a>c):
    print("A is the greatest number",a)
elif(b>c):
    print("B is the greatest number",b)
else:
    print("C is the greatest number",c)

print("-------------------------------------------------")