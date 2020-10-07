var = 6
var1 = 56

print("enter a number")
var2 = int(input())

if var2 > var1:
    print("greater")
elif var2==var1:
    print("equal")
else:
    print("lesser")

list1 = [5, 7, 3]
if 7 in list1:
    print("yes it's in the list")
else:
    print("no it's not in the list")

print(7 in list1)
print(14 in list1)
print(7 not in list1)
print(14 not in list1)

print("please enter your age")
age = int(input())

if age > 18 and age < 110:
    print("you can drive")
elif age > 110 or age == 0:
    print("wrong input")
else:
    print("you can't drive")


# short hand if else notation

a = int(input("enter\n"))
b = int(input("enter\n"))

# if a > b: print("a is greater then b")

print("b is greater then a") if b > a else print("a is greater then b")