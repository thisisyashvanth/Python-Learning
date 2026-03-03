# Ordered, Mutable, Can store mixed types, Dynamic size

data = [1, "Yashvanth", 158]

print(data[0])
print(data[-1])

data.append(54.4)
data.extend(["Acxhange", True])
data.insert(2, "Chennai")

# data.pop()
# data.pop(0)
# data.remove("Chennai")

print(data)

for n in data:
    print(n)


num_list = [5,4,2,3,6,2,9]
num_list.sort()
print(num_list)

sorted_num_list = sorted(num_list)
print(sorted_num_list)