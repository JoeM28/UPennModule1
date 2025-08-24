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
list2=[5,3,8,-1,-2.2,0]
print(list2)
print(list2[0])
temp= list2[0]
for number in list2:
    if number < temp:
        print(f"Small number {number} is here")
        temp = number
print(f"After all in list2 smallest number is {temp}")
planets = ['earth','venus','mercury','mars']
for plan in planets:
    if (plan == 'earth'):
        print(f"Earth is a living planet: {plan}")
    elif (plan == 'venus'):
        print(f"Venus is a small planet: {plan}")
    else:
        print(f"Normal planet: {plan}")
month='January'
print(month ,len(month)," Is the month ")
for x in month:
    print (x)
print("hello")
for x in month:
    print (x,end=' ')
print()
# name = input("What is your name? ")
name = 'gary'
print(name)
lettercount=0
for x in name:
    print(x, end=' ')
    lettercount += 1
print(lettercount)

for x in range(5,15):
    print(x)
for x in range(10):
    print(x)
for x in range(19,20):
    print(x)
for x in range(0,30,5):
    print(x)
for x in range(18,4,-2):
    print(x)
odd=[]
even=[]
for x in range(1,1201):
    if x % 2 != 0:
        odd.append(x)
    else:
        even.append(x)
print(odd)
print(even)
a = 5
while (a > 0):
    print("A is decremented : ", a)
    a=a-1
print(a)

x=4
while (x < 64):
    x = 2 *x
    print(x)

inp = "hello"

#inp = input("Say hello...")
while inp != "hello":
    inp = input("Say hello...")
print ("We got hello")

#password=""
password = "secret"
print(password)
while password != "secret":
    password = input("Say Password...")
    if password == "secret":
        print("Welcome")
    else:
        print("Try again")

x=1
while x < 10:
    if x == 5:
        print("Got 5 breaking")
        break
    else:
        print(x)
    x=x+1

for num in range(1,15):
    if (num % 2 != 0):

        if (num % 3 == 0):
           #print( "odd multiple of 3 " , num)
            continue
        print("odd not multiple of 3 " , num)

for i in range(1,3):
    print(i)
    for j in range(11,13):
        print(j)
    print(i,j)
for i in range(1,5):
    for j in range(1,5):
        print("{}  * {} = {}".format(i,j,j*i)  )

numlist =[]

num1= -1
while num1 != -1:
    #num1=int(input("Pls enter a number hit -1 to complete : "))
    numlist.append(num1)
val= 0
for num in numlist:
    val = val + num
count=len(numlist)
avg=0
#avg = val/count
print ("value total {}  Count Total{} Avg Total {}".format(val,count,avg))
str1="temporary"
print(str1)
l=len(str1)
print(l)
rev=''
for letter in str1:
    print(letter, end='')
for j1 in range(l-1,-1,-1):
    print(j1)
    rev += str1[j1]
print(rev)
for i in range(1,5):
    print(i)
x=548
print(float(x))
x=43.549894
print(round(x,2))
print(max(46,22,98,14))
print(min(46,22,98,14))
print(len("Google"))

def square(x):
    y= x*x
    return y

result= square(30)
print(result)
print(square(5))

def grt_check(x,y):
    """ Returns True if greater"""
    if x > y :
        return True
    else:
        return False

a=5
b=21
if grt_check(a,b):
    print("grt")
else:
    print("not grt")

help(grt_check)
#print(grt_check.__doc__)

def get_fact(x):
    """ Returns the factor of x"""
    factors = []
    for i in range(1,x+1):
        if x % i == 0:
            factors.append(i)
    return factors

print(get_fact (52))


def unique_list(l):
    """ Returns a list of unique elements"""
    l21=[]
    for x in l:
        if x not in l21:
            l21.append(x)
    return l21

list1 = [32,1,32,1,3,22,11,33,22]
l22 = unique_list(list1)
print(l22)



def calc(a, b, c):
    print(a * b * c)

calc(25, 75, 55)
calc(10.2, 20.3, 4)
calc('output', 10.2, 20.3)

num = 10
i = 9
if num % i == 1:
    print(num)
    break