import turtle

t=turtle.Turtle()
t.shape("turtle" )
t.color('#84c5a6')  #цвет черепашки
t.speed(0) #скорость черепашки
turtle.bgcolor('black')

for i in range(0,150):
    t.fd(30+i)
    t.lt(91) #91, 120, 72, 92, 60. 91. 46
    t.circle(i)

turtle.exitonclick()