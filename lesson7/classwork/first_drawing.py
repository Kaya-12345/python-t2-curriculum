import turtle
 t = turtle.Turtle()
t.speed(3)

for i in range(4):
  t.forward(100)
  t.left(90)

t.penup()
t.goto(-150,0)
t.pendown()

for i in range(3):
  t.forward(120)
  t.left(120)
