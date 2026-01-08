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
name = input("What is your name ? ")
age = int(input("How old are you ? "))
age = age + 1
print(f"Hello {name}")
print("Happy Bday")
print(f"Age: {age}")