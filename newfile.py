import turtle

s=turtle.Screen().bgcolor('black')
t=turtle.Turtle()
t.speed(10)
t.width(5)

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

def heart():
    t.color("red","red")
    t.begin_fill()
    t.left(130)
    t.forward(113)
    curve()
    t.left(130)
    curve()
    t.forward(112)
    t.end_fill()

heart()

t.penup()
t.goto(-270,-20)
t.pencolor("red")