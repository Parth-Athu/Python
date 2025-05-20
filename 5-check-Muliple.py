print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("  ~~ Check if a Number is a Multiple ~~ ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

a = int(input("Enter a Number(to check): "))
b = int(input("Enter Table Number: "))

print("--------------------------------------------")
print("You entered: Number =", a, " | Table of =", b)
print("-----------------------------------------_--")

if(a % b==0 ):
    print(a," is multiple of ",b)
else:
    print(a,"is not a multiple of ",b)

print("-------------------------------------------")