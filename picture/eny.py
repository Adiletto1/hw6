import turtle
turtle.speed(40)
turtle.color('cyan')
turtle.bgcolor("black")
b = 200
while b > 0:
    turtle.left(b)
    turtle.forward(b*3)
    b = b - 1