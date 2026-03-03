# Python allows top-level functions (not necessary to be inside a class).

def greet(name, prefix="Hello"):
    print(prefix, name)

greet("Yash")


def create_user(name, age, city):
    print(name + " " + str(age) + " " + city)    
    
create_user(age=22, name="Yash", city="Chennai")


def sum_all(*numbers):
    print(sum(numbers))

sum_all(1, 2, 3, 4)


# Type Hints/Annotations (Optional Typing)
def add(a: int, b: int) -> int:
    return a + b
