import math

# First Python Program
print("I like biriyani")
print("It's really good")
print()


# Variables
# Strings
first_name = "Yashvanth"
food = "Biriyani"
email = "yash@gmail.com"
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")
print()

# Integers
age = 22
quantity = 3
num_of_students = 30
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")
print()

# Float
price = 10.99
gpa = 3.2
distance = 3.5
print(f"The price is {price}")
print(f"Your gpa is {gpa}")
print(f"You ran {distance} KM")
print()

# Boolean
is_student = True
for_sale = False
print(f"Are you a student ? {is_student}")

if for_sale:
    print("That item is for sale")
else:
    print("That item is not available")
print()


# Typecasting
name = "Yashvanth"
age = 22
gpa = 3.2
is_student = True

gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

age = str(age)
print(age)

name = bool(name)
print(name)

print(type(name))


# input 
# name = input("What is your name ? ")
# age = int(input("How old are you ? "))
# age = age + 1
# print(f"Hello {name}")
# print("Happy Bday")
# print(f"Age: {age}")
# print()


# arithmetic and math
x = 3
y = 2
z = x**y
print(f"{x}**{y}={z}")

x = 10
y = 3
z = x % y
print(f"{x}%{y}={z}")

x = 3.14
y = -5
z = 5
print(f"Rounded: {round(x)}")
print(f"Absolute: {abs(y)}")
print(f"Power: {pow(2,2)}")
print(f"Maximum: {max(x,y,z)}")
print(f"Minimum: {min(x,y,z)}")

x = 9
y = 9.1
z = 9.9
print(f"PI: {math.pi}")
print(f"Square Root: {math.sqrt(x)}")
print(f"Ceil: {math.ceil(y)}")
print(f"Floor: {math.floor(z)}")
print(f"PI Rounded to two places: {round(math.pi, 2)}")
print()


# String Slicing
word = "Yashvanth T V"
first_letter = word[0]
nick_name = word[0:4] #nick_name = word[:4]
initial = word[10:13] #initial = word[10:]
reversed_word = word[::-1]
print(f"First Letter: {first_letter}")
print(f"Sliced Name: {nick_name}")
print(f"Initial: {initial}")
print(f"Reversed: {reversed_word}")

website1 = "http://google.com"
website2 = "http://wikipedia.com"
sliced = slice(7,-4)
print(f"Using slice function: {website1[sliced]}")
print(f"Using slice function: {website2[sliced]}")
print()


# If Statements
age = 10
if age <= 0:
    print("Enter a valid age")
elif age <= 18:
    print("You are a child")
else:
    print("You are an adult")
print()


# Logical Operators
temp = 10
if temp >= 0 and temp <= 30:
    print("Temp is good")
elif temp < 0 or temp > 30:
    print("Temp is bad")

a = 9
if not(a > 10):
    print("It is less than 10")
print()


# While Loop
# name = None
# while not name:
#     name = input("Enter your name: ")
# print(name)


# For Loop
for i in range(10):
    print(i+1)
print()

for i in range(11, 21):
    print(i)
print()

for i in range(0,101,10):
    print(i)
print()

for i in "Yash":
    print(i)
print()


# Nested Loops
rows = 3
cols = 3
symbol = "*"
for i in range(rows):
    for j in range(cols):
        print(symbol, end="")
    print()
print()


# Loop Control Statements

while True:
    name = input("Name: ")
    if name != "":
        break

phone_number = "91-90232434"
for i in phone_number:
    if i == "-":
        continue # Skips to the next iteration of the loop
    print(i, end="")
print()

for i in range(1,6):
    if i == 3:
        pass
    else:
        print(i, end=" ")