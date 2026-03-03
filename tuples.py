# Ordered, Immutable, Allows Duplicates, Access by Index

t1 = 1,2,3 
t2 = (1,2,3)
t3 = 1,
t4 = (1,)
print(type(t1)) # <class 'tuple'>
print(type(t2)) # <class 'tuple'>
print(type(t3)) # <class 'tuple'>
print(type(t4)) # <class 'tuple'>

t = (1, 2, 3)
t[0] # 1
t[0] = 99 # Error

# Tuple Unpacking
a, b = (10, 20)
a, b = b, a