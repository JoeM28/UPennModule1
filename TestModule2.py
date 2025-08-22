list1 = ['cat','dog',1,2,3]
print(list1)
print(len(list1))
print(list1[0])
print(list1[1])
list1.append('lion')
print(list1)
list1.pop() #removes LAST ITEM
print(list1)
list1.remove('dog') # removes particular element
print(list1)
list1.pop(1)  #removes index 1
print(list1)
print('cat' in list1) # returns boolean True if present
num = [1,2,3,4,5,6,7,8,9,10]
list2=[]
listeven1=[]
listodd1=[]
for number in num:
    list2.append(number)
    print(number)
print(list2)
for n1 in list2:
    if n1 % 2 == 0:
        print(f"Even number {n1} is here")
        print("Even Number",n1)
        print("Even Number"+ str(n1))
        listeven1.append(n1)
    else:
        print(f"Odd number {n1} is here")
        listodd1.append(n1)
print(listeven1)
print(listodd1)
