names = ["hari", "viplove", "rahul", "jack", "harry", 96]
print(names[2])

numbers = [5, 7, 8, 4, 6, 10]
print(numbers[2])
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(names[0:6:2])
print(names[::-1])
print(names[0:6:-1])

print(len(names))
print(max(numbers))
print(min(numbers))

names.append("carry")
numbers.append(7)
print(numbers)
print(names)

names.pop()
numbers.pop()
print(numbers)
print(names)

names.insert(2, "ajay")
numbers.insert(3, 11)
print(numbers)
print(names)

names.remove("viplove")
numbers.remove(6)
print(numbers)
print(names)

# touples in python

rollno = (1, 2, 3, 4, 5, 6, 7)
print(rollno)
print(type(rollno))