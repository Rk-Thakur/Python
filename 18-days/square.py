from turtle import Turtle, Screen

tim = Turtle()

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()




my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()