# This is where we left off of the Turtle project
# from turtle import Turtle, Screen
#
# ted = Turtle()
# ted.shape("turtle")
# ted.color("PaleTurquoise1")
# ted.pencolor("red")
# ted.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
table.horizontal_char = "~"
print(table.get_string(sortby="Pokemon Name", reversesort=False))
