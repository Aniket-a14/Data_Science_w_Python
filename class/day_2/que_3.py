# Break statement
print("Numbers are: ",end="")
for i in range(10):
    if i == 5:
        break
    print(i,end=" ")



# Continue statement
print("\nNumbers are: ",end="")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i,end=" ")



# Pass statement
print("\nNumbers are: ",end="")
for i in range(10):
    if i == 5:
        pass
    else:
        print(i,end=" ")



# Nested loops
for i in range(3):
    for j in range(3):
        print(i, j)




#match-case statements
status_code = 404

match status_code:
    case 200:
        print("OK")
    case 201:
        print("Created")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case _:
        print("Unknown Status")
