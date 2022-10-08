shopping = []
c = 1
while(c!=0):
    shopping.append(input("Enter item : "))
    print("continue : 1")
    print("End : 0")
    c = int(input("Enter choice : "))
for item in shopping:
    print(item)