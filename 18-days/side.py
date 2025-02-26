import turtle as t
import random 

tim  = t.Turtle()

color =['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen','wheat','SlateGray','SeaGreen']

def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range (num_sides):
        tim.forward(100)
        tim.right(angle)
        
for shape_side_n in range(3,11) : 
    tim.color(random.choice(color))
    draw_shapes(shape_side_n)   