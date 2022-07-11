#Name: Isong Mbah
#Date: Thu Jul 11 2022
#Project: Chapter 5 Point of Sale program

#declareGlobals here
def initializeGlobals():
    global pizza_price, fries_prize, drinks_price, tax

    pizza_price = 5.95
    fries_prize = 3.95
    drinks_price = 2.75

    round(pizza_price, 2)
    round(fries_prize, 2)
    round(drinks_price, 2)

# function to print error messages on the screen
def printError(error_message):
    print(f"Error: {error_message}")

#function to display menu
def displayMenu():
    print("******My Fast Food Hut ******")
    print(" P) izza slices\n F) ries\n D) rinks\n T) otal\n E) xit")

    selected = input("Enter letter: ")
    if selected == "p":
        return selected
    elif selected == "f":
        return selected
    elif selected == "d":
        return selected
    elif selected == "t":
        return selected
    elif selected == "e":
        return selected
    else:
        error_message = "Not valid selection"
        printError(error_message)

# function to get the quantity of a food
def getQuantity(food_type):

    if food_type == "Pizza slices":
        qtFood = int(input(f"How many {food_type}: "))
        return qtFood
    if food_type == "Fries":
        qtFood = int(input(f"How many {food_type}: "))
        return qtFood
    if food_type == "Drinks":
        qtFood = int(input(f"How many {food_type}: "))
        return qtFood
    

#function to print the bill
def printBill(qtPizza, qtFries, qtDrinks):

    #Calculating total price of items
    total_price = (pizza_price * qtPizza) + (fries_prize * qtFries) + (drinks_price * qtDrinks)

    #calculating the tax
    tax = (8.5 * total_price) / 100

    #calculating total price including taxt price
    sum_total = total_price + tax

    #rounding the total price and tax to 2 decimal places
    round(total_price, 2)
    round(tax, 2)
    round(sum_total, 2)
    
    print("Item                 Qty             Price")
    print(f"Pizza slices        {qtPizza}                {pizza_price * qtPizza}")
    print(f"Fries               {qtFries}                {fries_prize * qtFries}")
    print(f"Drinks              {qtDrinks}                {drinks_price * qtDrinks}")
    print(f"Tax                                  {tax:.2f}")
    print(f"                                    .............")
    print(f"Total                                {sum_total}")
    print(f"                                    =============")

def main():
    #initialize globalsp
    initializeGlobals()
    
    #declare local quantity variables
    qtPizza = 0
    qtFries = 0
    qtDrinks = 0

    #loop main tasks
    flag = True
    while flag:
        selection = displayMenu()

        if selection == "p":
            qtPizza = getQuantity("Pizza slices")
        elif selection == "f":
            qtFries = getQuantity("Fries")
        elif selection == "d":
            qtDrinks = getQuantity("Drinks")
        elif selection == "e":
            flag = False
        else:
            printBill(qtPizza, qtFries, qtDrinks)
            qtPizza = 0
            qtFries = 0
            qtDrinks = 0
            
if __name__ == "__main__":
    main()



    
        
        
