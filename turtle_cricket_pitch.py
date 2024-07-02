import turtle
bg = turtle.Screen()
bg.bgcolor("green")


amrit = turtle.Turtle()
amrit.color("lightpink")

gunnu =turtle.Turtle()
gunnu.color("white")

saanvi = turtle.Turtle()
saanvi.color("white")

lucky = turtle.Turtle()
lucky.color("white")

mummy = turtle.Turtle()
mummy.color("white")

baba = turtle.Turtle()
baba.color("white")

bubhu = turtle.Turtle()
bubhu.color("white")


amrit.begin_fill()
amrit.penup()
amrit.goto(250,0)
amrit.pendown()
amrit.left(90)
amrit.forward(900)
amrit.left(90)
amrit.forward(510)
amrit.left(90)
amrit.forward(1800)
amrit.left(90)
amrit.forward(510)
amrit.left(90)
amrit.forward(900)
amrit.end_fill()

gunnu.penup()
gunnu.goto(-700, -700)
gunnu.pendown()
gunnu.forward(2000)

saanvi.penup()
saanvi.goto(-700,700)
saanvi.pendown()
saanvi.forward(2000)

mummy.penup()
mummy.goto(175,700)
mummy.pendown()
mummy.left(90)
mummy.forward(200)

lucky.penup()
lucky.goto(-185,700)
lucky.pendown()
lucky.left(90)
lucky.forward(200)

baba.penup()
baba.goto(175,-700)
baba.pendown()
baba.right(90)
baba.forward(200)

bubhu.penup()
bubhu.goto(-185,-700)
bubhu.pendown()
bubhu.right(90)
bubhu.forward(200)

turtle.mainloop()