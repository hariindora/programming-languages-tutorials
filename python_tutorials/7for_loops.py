list1 = ["hari", "viplove", "rahul", "jack", "harry", "rohan"]
t1 = ("hari", "viplove", "rahul", "jack", "harry", "rohan")
list2 = [["hari", 98], ["viplove", 76], ["rahul", 87], ["jack", 87], ["harry", 34], ["rohan", 45]]
dict1 = dict(list2)

for i in list1:
    print(i)

for i in t1:
    print(i)

for i in list2:
    print(i)

for name, marks in list2:
    print(name, "score", marks, "%")

for name, marks in dict1.items():
    print(name, "score", marks, "%")

for items in dict1:
    print(items)

items = ["harry", "jack", 5, 9, 5, 2, 8, 3, 8, 5, 2, 1]

for item in items:
    if str(item).isnumeric() and item > 4:
        print(item)