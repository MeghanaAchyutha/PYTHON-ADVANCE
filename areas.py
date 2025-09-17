def square(a):
    print("the area is",a**2)
def rectangle(a,b):
    print("The area is",a*b)
def circle(r):
    print("The area is",3.14*(r**2))
def triangle(a,b):
    print("The area is",1/2*(a*b))
while(1):
    print("--------------------")
    print("menu")
    print("1.square")
    print("2.rectange")
    print("3.circle")
    print("4.triangle")
    print("5.exit")
    choice = int(input())
    if choice == 1:
        a = int(input("enter the side of square: "))
        square(a)
    elif choice == 2:
        a = int(input("enter rectangle length: "))
        b = int(input("enter rectangle breadth: "))
        rectangle(a,b)
    elif choice == 3:
        r = int(input("enter the circle radius: "))
        circle(r)
    elif choice == 4:
        a = int(input("enter the base: "))
        b = int(input("enter the height: "))
        triangle(a,b)
    else:
        print("The program is exited")
        break
        


