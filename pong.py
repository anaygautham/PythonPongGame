import turtle


wn = turtle.Screen()
wn.title("Pong by me")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)

#score tracker
score1 = 0
score2 = 0

#paddle 1 code
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("black")
paddle1.shapesize(stretch_wid=5, stretch_len= 1)
paddle1.penup()
paddle1.goto(-350, 0)


#paddle 2 code
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("black")
paddle2.shapesize(stretch_wid=5, stretch_len= 1)
paddle2.penup()
paddle2.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
dx = 0.45
dy = -0.45

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align = "center", font=("Courir", 24, "normal"))


#Funtion
def paddle_1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

def paddle_1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)

def paddle_2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

def paddle_2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)

#keyboard input
wn.listen()
wn.onkey(paddle_1_up, "w") 
wn.onkey(paddle_1_down, "s") 
wn.onkey(paddle_2_up, "Up") 
wn.onkey(paddle_2_down, "Down") 

#game stuff
while True:
    wn.update()

    #ball movement
    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)

    #border check

    if ball.ycor() > 290:
        ball.sety(290)
        dy *= -1
        
    
    if ball.ycor() < -290:
        ball.sety(-290)
        dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        dx *= -1
        score1 += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score1, score2), align = "center", font=("Courir", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        dx *= -1
        score2 += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score1, score2), align = "center", font=("Courir", 24, "normal"))

    # when the paddel and ball touch

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        ball.setx(340)
        dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-340)
        dx *= -1
    