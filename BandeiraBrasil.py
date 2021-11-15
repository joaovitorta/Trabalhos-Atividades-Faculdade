import turtle
t=turtle.Turtle()

t.fillcolor('green')

t.begin_fill()
t.setposition(100,0)
t.setposition(100,100)
t.setposition(-100,100)
t.setposition(-100,0)
t.setposition(0,0)
t.end_fill()

t.fillcolor('yellow')
t.begin_fill()
t.setposition(100, 50)
t.setposition(0,100)
t.setposition(-100, 50)
t.setposition(0,0)
t.end_fill()

t.penup()
t.setposition(0,25)
t.pendown()

t.fillcolor('Blue')
t.begin_fill()
for a in range(0,90):
  t.forward(2)
  t.left(4)

t.end_fill()
