#Name: Isong Mbah
#Date: Thu Jun 23 2022
#Project: Chapter 3 assignment on relational operators and conditional statements

#user input food name
food =  input("Please enter name of food: ") 

#user input calories per serving
caloriesPerServing = float(input("Please enter total calories per serving: ")) 

#user input grams of fat per serving
gramsOfFatPerServing = float(input("Please enter grams of fat per serving: "))

#calculating percentage of calories from fat
percentagOfCaloriesFromFat =(((gramsOfFatPerServing * 9) / caloriesPerServing) * 100)

#printing the percentage output of calories from fat
print(f'{food} contains {percentagOfCaloriesFromFat:,.1f}% calories from fat')

#decision statements to determine if the food meets the AHA recommendations
if(percentagOfCaloriesFromFat > 30): print(f"{food} exceeds the AHA recommendation.")
else: print(f"{food} meets the AHA recommendation.")