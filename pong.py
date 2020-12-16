import turtle

# Create a windows
wn = turtle.Screen()
wn.title("Pong by Meg Rocha")
wn.bgcolor("white")
wn.setup(width = 800, height = 600)
wn.tracer(0)

# Paddle A
    # small t for the turtle and Big T for class name in Turtle
paddle_a = turtle.Turtle()
    # speed of animation
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

# Main game loop
while True:
    wn.update()

# Move ball
ball.setx(ball.xcor()+ ball.dx)
ball.sety(ball.xcor()+ ball.dy)

# Border
if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1

if ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1

if ball.xcor() > 390:
    ball.goto(0,0)
    ball.dx *= -1

if ball.xcor() < -390:
    ball.goto(0,0)
    ball.dx *= -1

# Paddle and ball collisions
if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor) -40 :
    ball.setx(340)
    ball.dx *= -1

if (ball.xcor() > -340 and ball.xcor() < -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor) -40 :
    ball.setx(-340)
    ball.dx *= -1

