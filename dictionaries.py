# basic operations
student = {'name': 'Dayo', 'age': 21, 'courses': ['Math', 'CompSci']}

print(student)  # print the whole set

print(student['name'])  # access an element of the set

print(student.get('phone', 'Not Found')) # access an element of the set with get method and specify default msg

student.update({'name':'Dayo Ajayi', 'phone-number':'785.578.5748'})    #update a set
print(student)

# ***********
# iterations
# ***********
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)