# Basic function defination
def my_function():
    print('Hello World')

my_function()


def print_name(first, last):
    print(first + ' ' + last)

print_name('Ajay', 'Kumar')


def unknow_argument(*args):
    print(args)

unknow_argument(1,2,3, 'one', 'two')

def named_arguments(age, gender, name):
    print(name + ' ' + str(age) +' '+ gender)

named_arguments(name='Ajay', age=21, gender='Male')

def unknown_named_arguments(**args):
    print(args)

unknown_named_arguments(age=21, gender='Female')