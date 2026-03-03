class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hi {self.name}. Your age is {self.age}")
    
    # def __str__(self):
    #     return f"{self.name}, {self.age}"
    
p1 = Person("Yashu", 22)

print(p1.name)
p1.greet()

# Try without __str__ and with __str__
print(p1)