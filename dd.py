import turtle
t1 = turtle.Turtle()
turtle.screensize(400,300,"green")
turtle.screensize(400,300,"red")
turtle.screensize(400,300,"green")
t1.seth(30)
t1.forward(150)
t1.seth(10)
t1.forward(150)
t1.heading()
t1.hideturtle()
t1.setx(120)#横
t1.sety(-120)#竖
t1.circle(100,steps=5)
t1.circle(100,180)
t1.circle(100,180,steps=5)
t1.circle(100,180,steps=5)
turtle.home()
turtle.screensize(400,300,"red")
t1.begin_fill()
t1.circle(10)
t1.end_fill()
turtle.screensize(400,300,"blue")

turtle.circle(50,steps=5)


a=input()
if a=='':
    a='yes'
def t2(qwq):
    import turtle
    global t2
    t2=turtle.Turtle()
    # t2.hideturtle()
    t2.color('red')
    t2.goto(0,-50)
    t2.circle(50)
    t2.lt(90)
    t2.fd(50)
    t2.setx(-50)
    t2.rt(90)
    t2.fd(100)
    t2.lt(90)
    t2.goto(0,0)
    t2.forward(50)
    if qwq == 'yes' or qwq == 'Yes':
        t2.hideturtle()
t2(a)

