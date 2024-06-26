from turtle import Turtle, Screen

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ").lower()
y_position =[-70, -40, -10, 20, 50, 80]
colors = ["red","orange","blue","green","purple","yellow"]

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-240, y=y_position[turtle_index])

def move_forward():
    tim.forward(1)
    
screen.exitonclick()
