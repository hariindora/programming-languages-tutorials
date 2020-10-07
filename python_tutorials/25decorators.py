# def function1():
#     print("subscribe now")

# func2 = function1
# del function1
# func2()


# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum

# a = funcret(0)
# print(a)


# def executer(func):
#     func("this")

# executer(print)


def dec1(func1):
    def nowexec():
        print("executing now")
        func1()
        print("executed")
    return nowexec

@dec1
def who_is_hari():
    print("hari is a good boy")

# who_is_hari = dec1(who_is_hari)
who_is_hari()