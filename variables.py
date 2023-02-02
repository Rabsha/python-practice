# use of type()
var01 = 10
var02 = "Rabsha"
var03 = 40.2
print(type(var01))
print(type(var02))
print(type(var03))

# Use of Variables
a = 10
b = 15
c = a + b

print("The answare of a + b =", c)

var1 = 10
var2 = "Rabsha"
var3 = "50"
var4 = "60"
print("va1 is int and var2 is string", str(var1) + var2)
print("Add these values then Convert into Strings", str(int(var3) + int(var4)))
print("Convert into Strings these values and concat with each Other", str(var3) + str(var4))


#User Inputs
print("Enter Your Number")
inpunum = input()

print("Your Number is ", int(inpunum) + 60)

print("Enter your First number")
ainp = input()
print("Enter your Second Number", input())
binp = input()

print("Sum of these two numbers is ", int(ainp) + int(binp))