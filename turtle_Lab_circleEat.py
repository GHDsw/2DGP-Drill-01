import turtle
import random

def move():
    #turtle.setheading(90)
    turtle.forward(50)

cx,cy,cr = random.randint(-200,200),random.randint(-200,200), random.randint(50,100)

turtle.penup()
turtle.goto(cx,cy)
turtle.pendown()
turtle.circle(cr)
turtle.penup()
turtle.goto(0,0)

tx,ty=turtle.position()

turtle.onkey(move,'w')
turtle.listen()

turtle.mainloop()

