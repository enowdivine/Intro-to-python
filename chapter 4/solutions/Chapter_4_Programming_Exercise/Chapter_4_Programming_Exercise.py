#Name: Isong Mbah
#Date: Fri July 1 2022
#Project: chapter 4 programming exercise on python program loops

# Requesting user user input
speed = float(input("Enter speed in miles per hour: "))
time = float(input("Enter time travelled in hours: "))

#initializing the counter variable
counter = 1

while counter <= time:
    distance = speed * counter
    print(f"Distance in {counter} hour is: {distance}")
    counter = counter + 1
   