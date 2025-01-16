import numpy as np

def calcMarks():

 n= list(map(int, input().split()))

 # avg=0
 # for i in range(len(n)):
 #     avg+=n[i]
 # avg/=len(n)

 avg= sum(n)/len(n)

 if avg>=90 and avg<=100:
    print(f"Average Grade: {avg}")
    print("Letter Grade: A")
 elif avg>=80 and avg<90:
    print(f"Average Grade: {avg}")
    print("Letter Grade: B")
 elif avg>=70 and avg<80:
    print(f"Average Grade: {avg}")
    print("Letter Grade: C")
 elif avg>=60 and avg<70:
    print(f"Average Grade: {avg}")
    print("Letter Grade: D")
 else:
    print(f"Average Grade: {avg}")
    print("Letter Grade: F")

num = int(input("Enter number of students: "))
for i in range(num):
   calcMarks()