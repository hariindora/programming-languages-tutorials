# i = 0

# while (True):
#     if i+1 < 5:
#         i = i+1
#         continue   #skip the rest of the code inside a loop for the current iteration only. Loop does not terminate but continues on with the next iteration.
#     print(i+1, end=" ")
#     if(i==44):
#         break   #stop the loop
#     i = i+1

while(True):
    inp = int(input("enter a number\n"))
    if inp > 100:
        print("congrates you have entered a number greater than 100\n")
        break
    else:
        print("try again\n")
        continue