#Name: Isong Mbah
#Date: June 16 2022
#Project: Average scores of three teams. A program that takes the input value of scores 
#         of three sports teams and calculate the average score

import turtle

first_game_scores = int(turtle.numinput("input", "Enter first game score"))
second_game_scores = int(turtle.numinput("input", "Enter second game score"))
third_game_scores = int(turtle.numinput("input", "Enter third game score"))

average_score = ((first_game_scores + second_game_scores + third_game_scores) / 3)

print(f'{average_score:.2f}')