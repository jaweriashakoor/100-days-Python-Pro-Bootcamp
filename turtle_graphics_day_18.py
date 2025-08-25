from turtle import Turtle , Screen
timmy=Turtle()
timmy.shape("turtle")
timmy.color("Red","Green") 

                                          # draw sqaure by moving turtle

# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90) # right and left value is given in angle or degrees
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
                                            # OR
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
# rename the variable by write click and then clicking rename symbol

                                         # draw a dashed line
for _ in range (20):
    timmy.pendown()
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)
    
    

screen=Screen()
screen.exitonclick()