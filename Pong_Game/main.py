import turtle, paddle, ball, time, scoreboard

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG GAME")
screen.tracer(0)

r_paddle = paddle.Paddle((-350,0))
l_paddle = paddle.Paddle((350,0))

ball = ball.Ball()

score = scoreboard.Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(0.5)
    screen.update()
    ball.move()
    
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -340 :
        ball.bounce_x()
        
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        
    if ball.xcor() > -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()