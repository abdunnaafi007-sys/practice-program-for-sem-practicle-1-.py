def rectangle():
    l = float(input("length:"))
    b = float(input("breadth:"))
    print("area of rectangle=",l*b)
def square():
    a = float(input("enter side of square:"))
    print("area of square=",a*a)
def circle():
    r = float(input("enter a radius of circle:"))
    area = 3.14*r*r
    print("area of circle=",area)
def triangle():
    base = float(input("enter base value:"))
    het = float(input("enter height value:"))
    area_tri = 0.5*base*het
    print("area of triangle=",area_tri)
print("1- area of rectangle")
print("2- area of square")
print("3- area of circle")
print("4- area of triangle")
c = int(input("enter your chooise:"))
if (c==1):
    rectangle()
elif (c==2):
    square()
elif (c==3):
    circle()
elif(c==4):
    triangle()
else:
    print("invalid input")
