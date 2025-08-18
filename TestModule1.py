print("Hello world")
print("Good Day", end=" ")
print("Whatsup ")
print("I'm going to go "," what is this",sep =":::::")
print("I'm going to go")
print(7/2)
print("7/2")
print(7//2)
print( 4.1 // 2)
print(7%3)
print(3.1%3)
print( 1 == 1)
print ("car" == 'car')
print(True)
print(bool(False))
print(bool(7 == 6))
print (( 500 %2 ) == 0)
print((501 % 2) >= 1)
print ("test " + "my work")
print ( type( 1001))
print( type ( "hello"))
print( type( "John" + "Taylor"))
print ( "Name : " + "Brandon\'s name")
print ( 12374/621)
print(int(12374/621))
print(round(12374/621))
print(int("1"))
print(5/2)
print("4%2" , 4%2)
print("4%2" + str(4%2))
print("Is Even : " + str( 4%2 == 00))
x=y=10
print( x)
z= 2* ( x+y)
print (z)
z= z** ( y-1)
print(z)
x=42
b = 15 < ( x/2) < 10
print ( b)
print( type(b))

x= 42
y= str(x)
x *= 2
y *= 2  #y = y *2
print(x)
print(y)
fav_mov=" Tom Cruise MI"
fav_singer="Mich Jackson"
fav=  fav_mov + fav_singer
favs = "Your fav move is " + fav_mov + "Your fav singer is " +fav_singer
print(favs)
print(fav)
x="cats";
y="dogs"
print("Its raining " + x + " and "+ y)
"""
bill = float (input("Bill ?"))
tax = float(input("Tax ?"))
tip = float(input("Tip ?"))

tax_amt = bill * tax /100
total_amt = bill + tax_amt

tip_amt = total_amt * tip /100

grand_total = total_amt + tip_amt

#round
grand_total_round = round(grand_total, 2)

print( "TOTAL AMOUNT INCLUDING TAX:" , total_amt )
print("TOTAL TIP :" , tip_amt)
print("TOTAL BILL :" + str(grand_total_round))
print("TOTAL BILL :" , grand_total_round )
"""
"""
print("hello")
x= input("2+2 = ")
if (x.isnumeric()):
    x= int(x)
    if x > 4:
        print("large")
    elif x < 4:
        print("small")
    else:
        print("good")
else:
    print("not a number")
"""

"""
print("hello") 
x= input("2+2 = ")
#try to cast
try:
    x= int(x)
#catch exception
except ValueError as e :
    print("Input is not integer")
    print(e)
#There is no exception else is hit after except
else:
    if x > 4:
        print("large")
    elif x < 4:
        print("small")
    else:
        print("good")
"""

def sum_answer(a, b):
    return a + b

print("hello")
print(sum_answer(2, 3))
test = sum_answer(15,20)
print(test)