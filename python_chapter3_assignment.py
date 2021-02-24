import turtle

turtle.bgcolor('ivory')

w = turtle.Pen() #꽃잎
w.color('peachpuff')
w.fillcolor('white')
w.pensize(5)


g = turtle.Pen() #잎사귀, 가운데
g.color('darkolivegreen')
g.fillcolor('olivedrab')
g.pensize(5)

y = turtle.Pen() #수술
y.color('orange')
y.fillcolor('gold')
y.pensize(5)

radius = 100
w.ht()
g.ht()
y.ht()

#잎사귀 그리기

g.penup()
g.setx(90)
g.sety(-40)

g.setheading(-60)
g.pendown()
g.begin_fill()
for i in range(2): 
    g.circle(radius, 90)
    g.circle(radius / 2, 90)
g.end_fill()

g.penup()
g.setx(-120)
g.sety(10)

g.setheading(150)
g.pendown()
g.begin_fill()
for i in range(2): 
    g.circle(radius, 90)
    g.circle(radius / 2, 90)
g.end_fill()  

#꽃잎 그리기

w.penup()
w.setx(15)
w.sety(90)
w.setheading(45) 
w.pendown()

w.begin_fill()
for i in range(2): 
    w.circle(radius, 90)
    w.circle(radius / 2, 90)
w.end_fill()

w.penup()
w.setx(-50)
w.sety(80)
w.pendown()
w.setheading(110)

w.begin_fill()
for i in range(2): 
    w.circle(radius, 90)
    w.circle(radius / 2, 90)
w.end_fill()

w.penup()
w.setx(30)
w.sety(20)
w.pendown()
w.setheading(-30)
w.begin_fill()
for i in range(2): 
    w.circle(radius, 90)
    w.circle(radius / 2, 90)
w.end_fill()

w.penup()
w.setx(-15)
w.sety(-35)
w.pendown()
w.setheading(-90)
w.begin_fill()
for i in range(2): 
    w.circle(radius, 90)
    w.circle(radius / 2, 90)
w.end_fill()

w.penup()
w.setx(-70)
w.sety(15)
w.pendown()
w.setheading(180)
w.begin_fill()
for i in range(2): 
    w.circle(radius, 90)
    w.circle(radius / 2, 90)
w.end_fill()

#가운데 그리기
g.penup()
g.goto(-20,-15)
g.setheading(0)
g.pendown()
g.begin_fill()
g.circle(50)
g.end_fill()

#수술 그리기
for i in range(1,3):
    y.penup()
    y.setx(i*50-95)
    
    for j in range(1,3):
        y.sety(j*50-50) 
        y.setheading(0)
        y.pendown()
        y.begin_fill()
        y.circle(10)
        y.end_fill()
        y.penup()
       
y.goto(-20,25)
y.setheading(0)
y.pendown()
y.begin_fill()
y.circle(10)
y.end_fill()
y.penup()


"""타원 그리기 for문 참고(출처): https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=10402&docId=377624901&qb=7YyM7J207I2sIO2DgOybkCDqt7jrpqzquLA=&enc=utf8&section=kin.ext&rank=1&search_sort=0&spq=0"""
