import turtle as turtle_module
import random
tim = turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
color_list = [(202,164,109),(234,45,23)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    # tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)  
        tim.forward(500)
        tim.setheading(0)





screen = turtle_module.Screen()
screen.exitonclick()