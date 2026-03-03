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

# while True:
#     name = input("Name: ")
#     if name != "":
#         break

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
print("\n")


# Lists
foods = ["Pizza", "Biriyani", "Dosa"]
print(foods)

for i in foods:
    print(f"{i} ", end="")
print()

print(foods[1])
foods[1] = "Maggie"
print(foods[1])

foods.append("Idly")
foods.remove("Dosa")
foods.pop()
foods.insert(0,"Cake")
foods.sort()
foods.clear()


# 2D Lists
drinks = ["Coffee", "Tea"]
dinner = ["Pizza", "Biriyani"]
dessert = ["Cake", "Ice Cream"]
food = [drinks, dinner, dessert]
print(food)
print(food[0][1])
print()


# Tuples -> Ordered & Unchangeable, Group Related Data
student = ("Yash", 21, "Male")
print(student.count("Yash"))
print(student.index(21))
print()


# Set -> Un-Ordered, Un-Indexed, No Duplicate Values
utensils = {"spoon", "knife", "Fork"}
dishes = {"Bowl", "Plate", "Cup"}

utensils.add("Towel")
utensils.remove("Towel")
# utensils.clear()

utensils.update(dishes)
for i in utensils:
    print(i, end=" ")
print()

dining_table = utensils.union(dishes)
print(dining_table)


# Dictionary -> Changeable, Un-Ordered Collection of Unique Key:Value pairs.
capitals = {"USA":"Washington DC", "India":"Delhi"}
print(capitals.get("India"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
for key,value in capitals.items():
    print(key, value)

capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Las Vegas"})
print(capitals.items())
capitals.pop("Germany")
capitals.clear()
print()


# Indexing Operator
name = "yashvanth"
if (name[0].islower()):
    name.capitalize()
print(name)
print()


# Functions
def hello(name, age): # -> Parameters
    print(f"Hello {name}, Age: {age}")
name = "Yash"
age = 22
hello(name, age) # -> Arguements
print()


# Return Statement
def multiply(num1, num2):
    result = num1 * num2
    return result

val = multiply(2,3)
print(val)
print()


# Keyword arguements
def hello(first, middle, last):
    print(f"Hello {first}{middle} {last}")
hello(middle="vanth",first="Yash",last="T V")
print()


# Variable Scope
# LEGB -> Local, Enclosing, Global, Buil-In


# *args -> Packs all arguements into a tuple, used for varying number of parameters
def args(*args):
    return args

print(args(1,2,3,4,5))


# **kwargs ->  Packs all arguements into a dictionary, used for varying number of keyword arguements
def hello(**kwargs):
    print(f"{kwargs["first"]}{kwargs["last"]}")
hello(last="vanth", first="Yash")
print()


# str.format()
animal = "cow"
item = "moon"
print("The {} jumped over the {}".format(animal, item)) 
print("The {1} jumped over the {0}".format(animal, item)) #positional argument
print("The {item} jumped over the {animal}".format(animal="cow", item="moon")) #positional argument
print("The {item} jumped over the {animal}".format(animal="cow", item="moon")) #positional argument
num = 3.1435235
print("{:.2f}".format(num))
print()


# Exception Handling
try:
    num1 = 10
    num2 = 0
    res = num1/num2
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(res)
finally:
    print("This will always execute")
print()


# Modules -> File containing code.
# import modulename
# import modulename as alias
# from modulename import code1, code2
# from modulename import *


# POOP

class Car:

    wheels = 4 # class variables -> Within class outside constructor, shared for all objects

    # self -> object that is using this method

    # Constructor
    def __init__(self, make, model):
        self.make = make #instance variable, unique for each object
        self.model = model #instance variable, unique for each object

    def drive(self):
        print(f"{self.model} is driving")
    def stop(self):
        print(f"{self.model} is stopping")

car1 = Car("Chevy", "Corvette")
print(car1.make, car1.model)
car1.drive()
car1.stop()


# Inheritance
class Animal:

    alive = True
    
    def eat(self):
        print("The animal is eating")

    def sleep(self):
        print("Animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("Rabbit is running")
class Fish(Animal):
    def swim(self):
        print("Fish is swimming")

rabbit = Rabbit()
fish = Fish()

rabbit.eat()
rabbit.run()

fish.sleep()
fish.swim()


# Multi Level Inheritance -> Child class inherits another child class
class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()


# Multiple Inheritance -> Child Class derived from more than one parent class

class Prey:
    def flee(self):
        print("Animal flees")
    
class Predator:
    def hunt(self):
        print("Animal hunts")

class Deer(Prey):
    pass

class Lion(Predator):
    pass

class Fish(Prey, Predator):
    pass

deer = Deer()
lion = Lion()
fish = Fish()

deer.flee()
lion.hunt()

fish.flee()
fish.hunt()
print()


# Method Overriding
class Male:
    def greet(self):
        print("Hi")

class Female(Male):
    def greet(self):
        print("Hey")

female = Female()
female.greet()


# super keyword
class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w

class Square:
    def __init__(self, l, w):
        super().__init__(l,w)

class  Cube:
    def __init__(self, l, w, h):
        super().__init__(l,w)
        self.h = h