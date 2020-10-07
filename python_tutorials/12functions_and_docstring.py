a = 1
b = 3

c = sum((a, b))   #built-in function
print(c)

def function1(a, b):
    """This is a function which will calculate average of two numbers
    This function take two arguments and print value"""
    average = (a + b)/2
    print("the average of", a, "and", b, "is", average)

function1(4, 6)

def function2(a, b):
    """This is a function which will calculate average of two numbers
    This function take two arguments and return value"""                          #this is an doc string
    average = (a+b)/2
    return average

val = function2(9, 8)
print(val)

print(function2.__doc__)
print(function1.__doc__)

print(sum.__doc__)