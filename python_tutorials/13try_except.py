print("enter num 1")
num1 = input()
print("enter num 2")
num2 = input()
try:
    print("the sum of these two numbers is", int(num1) + int(num2))
except Exception as e:
    print(e)

print("this is very importent line")