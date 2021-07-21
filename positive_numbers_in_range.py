list1=[12, -7, 5, 64, -14]
for item in list1:
    if item <0:
        continue
    print(item,end=" ")

list2=[]
num=int(input("\nHow many values u want in list: "))
for i in range(num):
    value=int(input("Enter values here: "))
    list2.append(value)
for item in list2:
    if item <0:
        continue
    print(item,end=" ")
