numbers = ["3", "34", "64"]

# using map function:-
# numbers = list(map(int, numbers))

# using for loop:-
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# numbers[2] = numbers[2] + 1
# print(numbers)



# using map function with normal function:-
num = [2, 3, 5, 6, 76, 3, 3, 2]
# def sq(a):
#     return a*a

# square = list(map(sq, num))
# print(square)

# using map function with lambda function:-
# square = list(map(lambda x: x*x, num))
# print(square)

# another example of map function:-
# def square(a):
#     return a*a

# def cube(a):
#     return a*a*a

# func = [square, cube]
# for i in range(5):
#     val = list(map(lambda x: x(i), func))
#     print (val)


# ===============Filter===============

list1 = [1,2,3,4,5,6,7,8,9]

def is_greater_5(num):
    return num > 5

gr_than_5 = list(filter(is_greater_5, list1))
print(gr_than_5)

# ================Reduce==============

from functools import reduce

list2 = [1,2,3,4]

# using for loop:-
# num = 0
# for i in list2:
#     num = num + i
# print(num)

num = reduce(lambda x, y : x+y, list2)
print(num)