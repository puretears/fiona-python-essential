
'''
Top importance:
* No braces in Python
'''

'''
# 1. Variable
An object that can store values.
Syntax:
variable_name = value
'''
n = 10                      # int
pi = 3.14                   # float
half = 1 / 2                # float
name = "11"                 # str
str_ten = "10"              # str

# Naming conventions
# namingConventions  - Camel Case
# naming_conventions - Snake Case

#         Open bracket     Close bracket
numbers = [1, 2, 3, 4, 5, 6] # list

'''
# 2. Flow control
How to control branches in the program.

if condition1:
    statements
elif condition2:
    statements
else:
    statements
'''
if name == "11":
    print("name: ")
    print(name)
    print(".")
elif name == "Fiona":
    print("Fiona")
else:
    print("Other names")

'''
# 3. Loop control
## 3.1 for loop
## 3.2 while loop
'''
#   loop variable
for number in numbers:
    print(number)

for n in range(1, 6):
    print(n)

i = 0
while i < 6:
    print(numbers[i])
    i = i + 1

'''
# 4. Functions
Input:
Process:
Output:
'''
# Input: name
# Process: print the name
# Output: None
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

#       Parameters         Return value
def sum(x: int, y: int) -> int:
    return x + y


'''
# 5. Custom types
# How to present a student in Python?
'''
class Student:
    # Attributes of a student
    # name: str
    # age:  int
    # id:   str
    # sex:  str
    # height: float
    # Initialization method
    def __init__(self, name: str, age: int, iden: str, sex: str, height: float):
        self.name = name
        self.age = age
        self.iden = iden
        self.sex = sex
        self.height = height


# Press the green button in the gutter to run the script.
# Entry point
if __name__ == '__main__':
    print_hi('PyCharm')

    teacher = Student(name="11", age=40, iden="111011xxxx", sex="Male", height=178.0)
    print(teacher.name)
    print(teacher.iden)
