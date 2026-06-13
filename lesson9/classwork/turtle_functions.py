import turtle

t = turtle.Turtle()
t.speed(0)

def draw_polygon(sides,length):
  angle = 360 / sides
  for _ in range(sides):
    t.forward(length)
    t.left(angle)

t.color("blue")
draw_polygon(5, 80)

t.penup()
t.goto(-200,-50)
t.pendown()

t.color("red")
draw_polygon(12,40)

turtle.done()
