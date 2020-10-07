import turtle

a = 3
b = 4
c = 5


if a < b:
    print("OK")
if c < b:
    print("OK")
if a + b == c:
    print("OK")
if a**2 + b**2 == c**2:
    print("OK")

print(200*"-")

if a < b:
    print("OK")
else:
    print("NOT OK")
if c < b:
    print("OK")
else:
    print("NOT OK")
if a + b == c:
    print("OK")
else:
    print("NOT OK")
if a**2 + b**2 == c**2:
    print("OK")
else:
    print("NOT OK")

print(200*"-")

color = input("What color?: ")
width = input("What line width?: ")
t_size = input("What line length?: ")
shape = input("line, triangle, or square?: ")

t = turtle.Turtle()
t.color(color)
t.width(int(width))

if shape == "line":
    t.forward(float(t_size))
elif shape == "triangle":
    t.forward(float(t_size))
    t.right(120)
    t.forward(float(t_size))
    t.right(120)
    t.forward(float(t_size))
    t.right(120)
elif shape == "square":
    t.forward(float(t_size))
    t.right(90)
    t.forward(float(t_size))
    t.right(90)
    t.forward(float(t_size))
    t.right(90)
    t.forward(float(t_size))
    t.right(90)
else:
    print("INVALID SHAPE")

turtle.Screen().exitonclick()
