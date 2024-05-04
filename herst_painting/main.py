# import colorgram
import turtle as t
import random
t.colormode(255)
tim = t.Turtle()
# rgb_colors = []
# colors = colorgram.extract('image.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
    
# print(rgb_colors)

color_list = [(243, 242, 237), (139, 154, 214), (211, 215, 235), 
              (187, 153, 187), (227, 208, 226), (169, 175, 235), 
              (179, 174, 131), (224, 213, 128), (85, 109, 216), 
              (216, 227, 220), (212, 176, 211), (157, 175, 160), 
              (51, 92, 181), (157, 156, 78), (159, 102, 169), 
              (134, 75, 134), (29, 48, 166), (132, 112, 84), 
              (181, 199, 184), (211, 183, 177), (100, 123, 108), 
              (172, 198, 206), (101, 39, 98), (112, 137, 122), 
              (148, 120, 115), (97, 137, 155), (11, 40, 106), 
              (29, 45, 242), (67, 38, 81), (219, 212, 26)]
t.hideturtle()
t.speed("fastest")
t.setheading(225)
t.penup()
t.forward(300)
t.setheading(0)

for _ in range(10):

   for _ in range(10):
      t.dot(20,random.choice(color_list))
      t.penup()
      t.forward(50)

   t.left(90)
   t.forward(50)
   t.setheading(180)
   t.forward(500)
   t.setheading(0)


screen = t.exitonclick()