import time
print("Loops")
print("For Loop")


print("Numbers are: ",end="")
for i in range(1,6):
    print(i, end=" ")


time.sleep(2)
print("While loop")


count=1
print("Numbers are: ",end="")
while count<6:
    print(count, end=" ")
    count+=1
