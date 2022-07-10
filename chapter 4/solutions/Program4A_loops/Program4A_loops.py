#Name: Isong Mbah
#Date: Fri July 1 2022
#Project: Chapter 3 assignment on relational operators and conditional statements



#add your preamble data here without the above first line



#Do not change any of my lines of code or variable names!
#Only add the lines necessary to solve the problem given
#Do not break this file into individual py files. You need to only
#submit one py program.

#Place all of your solutions in this one file and submit to the appropriate
#link when complete.

#problem 1
#Counter controlled loops require three things to work:
# 1. an initialized counter variable      
# 2. a testing of the counter variable
# 3. increment/decrement of the counter variable
#Using variable counter, write a While loop that prints "Programming is FUN!"
#to the screen five (5) times.
from pprint import pprint
from turtle import numinput


counter = 0
while counter <= 4:
    print("Programming if FUN")
    counter = counter + 1
      
            
#problem 2
#Now repeat problem 1 using a For...loop and the range() function.
for counter in range(5):
    print("Programming is FUN")
      
      
#problem 3
#Write a For...loop that adds up the numbers 1 to 10 into a total variable.
#print the total to the screen.
total = 0
for counter in range(11):
    total = total + counter
print(f"Total is: {total}")


          
#problem 4
#Output the following to the screen using a For...loop and range()function.

#Counting at 5
#Counting at 4
#Counting at 3
#Counting at 2
#Counting at 1
for counter in reversed(range(6)):
    print(f"Counting at {counter}")
    counter = counter - 1


#problem 5
#Using the variable below create a While loop that prints the following
#to the screen:
#2 4 6 8 10 12 14 16 18 20
counter = 0
while counter <= 18:
    counter = counter + 2
    print(f"{counter}")
      
      
#problem 6
#Using the following variable, write the code necessary to add the total of all
#the values from 0 to 100 and print only the total after computing it.
#You can use any loop structure.
total = 0
for counter in range(101):
    total = total + counter
print(f"Total is: {total}")

      
               
#problem 7 
#Modify problem 6's code to do the same thing, but the maximum number
#(which was 100) should be entered by the user and stored in the variable
#maxNumber the loop. So, the user enters a number for the maximum range and all the
#values from 0 to the number entered, which is stored in maxNumber are totaled.
total = 0
maxNumber = int(input("Enter the maximum number: "))
for counter in range(maxNumber + 1):
    total = total + counter
print(f"Total is: {total}")

      
#problem 8
#Now modify problem 7 to allow the user to enter the range of numbers to be
#totaled beginning with the min value and the max value.     
#You will need to delcare and initialize variables minValue and maxValue for
#use with this problem. The keyboard is already declared. You will also
#need to create the prompts and input statements.
total = 0
minValue = int(input("Enter minimum value: "))
maxValue = int(input("Enter maximum value: "))
counter = minValue
for counter in range(minValue,  maxValue + 1):
    total = total + counter
print(f"Total is: {total}")
      
      
#problem 9
#Write the statements necessary to do the following: Total all the integer
#values a user enters into the computer until they enter -1. Once -1 has
#been entered exit the loop, display the total of the numbers entered. You
#must use a While...loop. Make certain no negative values are added to the
#total. Only exit on -1, not any other negative value.
total = 0
number_list = []

while True:
    number = float(input("Ente a number: "))
    if number == -1:
        break
    number_list.append(number)

# convert each item to int type
for i in range(len(number_list)):
    # convert each item to int type
    number_list[i] = int(number_list[i])

# calculating the sum
for counter in number_list:
    if counter < 0:
        continue
    total = total + counter

#printing the total
print(f"Total is: {total}")
      
#problem 10
#Recreate problem 9, but this time use a flag controlled loop. When the user
#enters a negative value, stop the loop and print the total.
total = 0
flag = True
number_list = []

while flag:
    number = float(input("Ente a number: "))
    if number < 0:
        flag = False
    number_list.append(number)

# convert each item to int type
for i in range(len(number_list)):
    # convert each item to int type
    number_list[i] = int(number_list[i])

# calculating the sum
for counter in number_list:
    if counter < 0:
        continue
    total = total + counter

#printing the total
print(f"Total is: {total}")





    
        
        
