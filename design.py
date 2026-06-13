# import turtle

# t=turtle.Turtle();
# s=turtle.Screen();
# s.bgcolor("black");
# t.speed(0)
# turtle.tracer(3,0)
# t.color("#D7CCC8")

# for i in range(400):
#     t.forward(i)
#     t.left(125)
#     t.forward(i)
#     t.left(45)


# turtle.done()
    # minimalist metallic geometric star

import turtle ,math,colorsys
screen = turtle.Screen();
screen.bgcolor("black")
screen.setup(800,800)
screen.title("rainbow web")
turtle.tracer(1,0)
t=turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(1)
n=100
m=3
h=0
for i in range(n):
    r,g,b = colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(r,g,b)
    t.penup()
    t.goto(300 * math.cos(2 * math.pi* i/n),
           300 * math.sin(2 * math.pi * i/n))
    t.pendown()
    j=(i*m) % n
    t.goto(300 * math.cos(2*math.pi * j/n),
           300 * math.sin(2*math.pi * j/n))
    h=(h+1 / n)% 1

turtle.done()
# mystic rose pattern 
