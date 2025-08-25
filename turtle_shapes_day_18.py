from turtle import Turtle , Screen
import random
timmy=Turtle()
colors=["red","green","blue","yellow","orange"]

def draw_shapes(number_of_sides):
    angle= 360 / number_of_sides
    for _ in range(number_of_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side_n in range(3,11):
    timmy.color(random.choice(colors))
    draw_shapes(shape_side_n)




screen=Screen()
screen.exitonclick()