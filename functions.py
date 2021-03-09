
def hello_func(greeting, name = 'You'):
    return f'{greeting}, {name}'

# print(hello_func('Hello'))


courses = ['Math', 'Art']
info = {'name':'Dayo', 'age':21}

def student_info(*args, **kwargs):      # positional and keyword arguments...
    print(args)
    print(kwargs)

student_info(*courses, **info)
student_info(courses, info)             # notice the difference in results between these two calls
