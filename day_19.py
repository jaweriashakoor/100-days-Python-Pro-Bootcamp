from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(10)

screen.listen()  # start listening for key presses
screen.onkey(key="space", fun=move_forward)  # bind spacebar to function

screen.exitonclick()