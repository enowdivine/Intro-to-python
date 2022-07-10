#Name: Isong Mbah
#Date: Thu Jun 23 2022
#Project: Chapter 3 assignment on relational operators and conditional statements

#add your preamble data here without the above first line



#Do not change any of my lines of code or variable names!
#Only add the lines necessary to solve the problem
#Do not break this file into individual py files.


#problem 1
#List, in comment form, all the relational operators and their functionality.

# > Greater than: This operator returns True if the left operand is greater than the right operand.
# < Less than: This operator returns True if the left operand is less than the right operand.
# == Equal to: This operator returns True if both the operands are equal i.e. if both the left and the right operand are equal to each other.
# != Not Equal to: This operator returns True if both the operands are not equal.
# >= Greater than or equal to: This operator returns True if the left operand is greater than or equal to the right operand.
# <= Less than or equal to: This operator returns True if the left operand is less than or equal to the right operand.

      
#problem 2
#List, in comment form, all the logical operators and their functionality.

# and: Returns True if both statements are true
# or: Returns True if one of the statements is true
# not: Reverse the result, returns False if the result is true

      
#problem 3
#Using the following variable - gpa and TWO IF statements, display the words
#With honors." when the gpa is greater than or equal 3.5 and
#"Without honors." when gpa is less than 3.5
gpa = 3.4 
if(gpa >= 3.5):
    print("With honors")
if(gpa < 3.5):
    print("Without homors")  

      
#problem 4
#Rewrite problem 3 using one If...else statement.
if(gpa >= 3.5):
    print("With honors")
else: print("Without honors")

      
#problem 5
#Using the following variable - number and TWO IF... statements determine if
#it's value is odd or even and display an appropriate message.
#Hint: remember modulo?
number = 5
if((number % 2) == 0): print("The number is even")
if((number % 2) != 0): print("The number is odd")

      
#problem 6
#Rewrite problem 5 using one If...else statement.
if((number % 2) == 0): print("The number is even")
else: print("The number is odd")

      
#problem 7
#Ask the user to enter a gpa value, store it in variable gpa. Create an
#if...elif statement, display the words "With honors" when the gpa is
#greater than or equal 3.5 and "Without honors" when gpa is less than 3.5
#and "Not valid" when the value is greater than 4.0.
gpa = float(input("Enter a value: "))
if(gpa >= 3.5 and gpa <= 4.0):
    print("With honors")
elif(gpa < 3.5):
    print("Without honors")
elif(gpa > 4.0):
    print("Not valid")


      
#problem 8
#Using the following variable and using one If...else statement and logical
#operator, print "Yes" to the screen if the number3 value is between 5 and 9
#and "No" if it is not.
number3 = 6
if(number3 > 5 and number3 < 9):
    print("Yes")
else: print("No")

      
#problem 9
#Using the following variables write the decision statements to answer the
#following scenario: A person qualifies for insurance when they are a
#non-smoker, veteran and over the age of 40. Print appropriate output to
#the screen.
age = 4
smoker = False
veteran = True

if(smoker == False and veteran == True and age > 40):
    print("The person is qualified")
else: print("The person is not qualified")

      
