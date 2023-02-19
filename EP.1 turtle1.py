import turtle
tt = turtle.Pen()
tt.shape('turtle')
tt.speed(0)

for i in range(30):
    tt.pencolor('#EB7070')
    tt.circle(i*1)
    tt.circle(i*2)
    tt.pencolor('#FEC771')
    tt.circle(i*3)
    tt.circle(i*4)
    
tt.up()
tt.setpos(0,200)
tt.down()
tt.rt(180)

for i in range(30):
    tt.pencolor('#E6E56C')
    tt.circle(i*1)
    tt.circle(i*2)
    tt.pencolor('#64E291')
    tt.circle(i*3)
    tt.circle(i*4)


tt.up()
tt.setpos(100,100)
tt.down()
tt.rt(90)


for i in range(30):
    tt.pencolor('#0E9577')
    tt.circle(i*1)
    tt.circle(i*2)
    tt.pencolor('#04DEAD')
    tt.circle(i*3)
    tt.circle(i*4)

tt.up()
tt.setpos(-100,100)
tt.down()
tt.lt(180)


for i in range(30):
    tt.pencolor('#F1EFB9')
    tt.circle(i*1)
    tt.circle(i*2)
    tt.pencolor('#FBFAE1')
    tt.circle(i*3)
    tt.circle(i*4)

tt.hideturtle()








