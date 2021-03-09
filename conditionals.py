language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')


user = 'Admin'
logged_in = False

if not logged_in:
    print('Please log in')
else:
    print('Welcome')


# illustrating the concept of 'is' to explain so
a = [1, 2, 3]
b = a 

print(id(a))
print(id(b))
print(a == b)
print(a is b)


# False values
# False
# None
# Zero of any numeric type
# Any empty sequence. For example '', (), []
# Any empty mapping. For example {}