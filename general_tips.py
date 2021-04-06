import sys
from collections import Counter
# Source: https://youtu.be/8OKTAedgFYg 
# 1. Iterate with enumerate() instead of range((len))
'''
data = [1, 2, -3, -4]

for i in range(len(data)):
    if data[i] < 0:
        data[i] = 0
print (data)

for index, value in enumerate(data):
    if value < 0:
        data[index] = 0
print(data)
'''

# 2 Use list comprehension instead of raw for loops
'''
squares = []
for i in range(10):
    squares.append(i*i)
print(squares)

squares = [i*i for i in range (10)]
print(squares)
'''

# 3 Sort complex iterables with sorted()
'''
data = [3,5,1,10,9]
sorted_data = sorted(data, reverse=True)
 
# also works for complex iterables: 
data = [{"name": "Max", "age":6},
        {"name": "Lisa", "age": 19}, 
        {"name": "Ben", "age": 9}]
sorted_data = sorted(data, key=lambda x: x["age"])
print(sorted_data)
'''

# 4 Store unique values with Sets
# Note: Sets also have some handy methods for calculating intersection
# and differences between two sets  
'''
my_list = [1,2,3,4,5,6,7,7,7]
my_set = set(my_list)
print (my_set)
'''

# 5 Save memory with Generators
'''
my_list = [i for i in range(10000)]
print (sum (my_list))
print(sys.getsizeof(my_list), "bytes")

my_gen = (i for i in range(10000))     # the only difference between this and list comprehension is the use of () instead of []
print (sum (my_gen))
print(sys.getsizeof(my_gen), "bytes")
'''

# 6 Define default values in Dictionaries with .get and .setDefault()
'''
my_dict = {"item":"football", "price": 10.00}
count = my_dict.get("count", 0) # note that my_dict["count"] throws a key error while a .get("count") will just return None, without throwing an error  
print (count)
count = my_dict.setdefault("count", 0)
print(count)
print(my_dict)
'''

# 7 Count hashable objects with collections.Counter
'''
my_list = [10,10,10,5,5,2,9,9,9,9,9,9,9]
counter = Counter(my_list)
print(counter)
print(counter[10])                      # handy to return the number of occurences of the given key
most_common = counter.most_common(2)    # SUPER handy to access the k-most occuring items
print (most_common[1][1])
'''

# 8 Format strings with f-strings
'''
name = "Dayo" 
my_string = f"Hello, {name}"
print(my_string)
'''

# 9 Concatenate strings with .join()
'''
list_of_strings = ["Hello", "my", 'friend']

# BAD!
my_string = ""
for i in list_of_strings:
    my_string += i + " "
print(list_of_strings)

# GOOD
my_string =  " ".join(list_of_strings)
print(list_of_strings)
'''

# 10 Merge two dictionaries with {**d1, **d2}
'''
d1 = {"name":"Dayo", "age": 25}
d2 = {"name":"Dayo", "City": "Dallas"}
merged_dict = {**d1, **d2}
print(merged_dict)
'''

# 11 Simplify if-statement with if x in [a,b,c]
colors = ["red", "green", "blue"]
c = "red"
if c in colors:
    print (c + " is indeed in the list!")

