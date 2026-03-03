# Key-value store, Keys must be hashable (Value that never changes during its lifetime), Insertion-ordered

data = {
    "name": "Yashvanth",
    "age": 22
}

# print(data["email"]) 
print(data.get("email"))
print(data.get("email", "NA"))

data["age"] = 21
data["city"] = "Chennai"

# data.pop("city")
# del data["age"]

for key in data:
    print(key, data[key])

for key, value in data.items():
    print(key, value)

print("name" in data)