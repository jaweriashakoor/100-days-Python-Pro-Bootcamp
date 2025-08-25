# # import turtle
# # timmy=turtle.Turtle()

# from turtle import Turtle,Screen # Trtle and Screen are the class
# timmy=Turtle() # timmy is object
# print(timmy)
# timmy.shape("turtle") # shape is object method
# timmy.color("red","green")
# timmy.forward(100)
# my_screen=Screen() #my_screen is object
# print(my_screen.canvheight) # canvasheight is the objcet attributes

# # functions when specific for object are known as object method 
# my_screen.exitonclick() # exitonclick is oject method

from prettytable import PrettyTable
table= PrettyTable()
table.add_column("Pokemon",["Pikachu","Squirtle","Charmander"]) 
table.add_column("Type",["Electric","Water","Water"])
table.align = "l"


print(table)