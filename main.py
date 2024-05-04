import turtle as t
import random

timmy = t.Turtle()

screen = t.Screen()

# timmy_the_turtle.shape("circle")
# timmy_the_turtle.width(20)
# timmy_the_turtle.color("red")
# for steps in range(100):
#     for c in ('blue', 'orange', 'green'):
#         timmy_the_turtle.color(c)
#         timmy_the_turtle.forward(steps)
#         timmy_the_turtle.right(90)

# direction = [0,90,180,270]
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color


def draw_circle(radius):
    t.pensize(1)
    t.speed('fastest')
    t.circle(radius)
    t.color('red')
    t.home()

for direction in range(0,360,10):
    t.left(direction)
    draw_circle(100)
    
    
# for _ in range(200):
#     timmy.speed('fast')
#     timmy.pensize(10)
#     timmy.setheading(random.choice(direction))
#     timmy.forward(30)
#     timmy.color(random_color())
    

screen.exitonclick()