#Name: Isong Mbah
#Date: June 16 2022
#Project: Point spread for two sport teams. A program that takes the input value of scores 
#         of two teams and calculate the point spread

import turtle

team_one = int(turtle.numinput("input", "Team one scores"))
team_two = int(turtle.numinput("input", "Team Two scores"))

pointspread = abs(team_one - team_two)

print(f'{pointspread}')