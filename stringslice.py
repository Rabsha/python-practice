#String Slicing
"""
String Start with 0 index
String Slicing start with [:]
first you Before SemiColumn means Including and After SemiColumn means Excluding
Find Length of string Use len()
For Example:
"""
Name = "I am Rabsha Shakeel"
NameNew = "IamRabshaShakeel"

print(len(Name))
print(Name[5::])

print("ok", Name.isalnum())
print("pk", NameNew.isalpha())
print(Name.count("a"))
print(Name.endswith("Shakeel"))