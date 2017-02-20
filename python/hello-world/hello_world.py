#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=''):
    if name == None:
        x = "World"
    elif name == '':
        x = "World"
    else:
        x = name

    greeting = "Hello, " + x + "!"
    return(greeting)
