# Ordered, Mutable, Allows Duplicate Keys but not values, Access by Key

person = {
    "name": "Yash",
    "age": 22
}

person["name"] # Yash

person["city"] = "Chennai" # Add

print(person.keys())
print(person.values())
print(person.items())

for k, v in person.items():
    print(k, v)

person.get("salary", 0) # Safe Access
