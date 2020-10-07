import time

initial = time.time()
print(initial)
for i in range(4):
    print("my name is hari")
    time.sleep(1)
print("for loop ran in:",time.time() - initial, "seconds")

time.sleep(2)

initial1 = time.time()
print(initial1)
i = 1
while(i<4):
    print("my name is hari")
    i+=1
print("while loop ran in:",time.time() - initial1, "seconds")

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)