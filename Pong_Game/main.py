from turtle import Turtle,Screen

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG GAME")
screen.exitonclick()

paddle = Turtle()
paddle.shape("sqaure")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350,0)