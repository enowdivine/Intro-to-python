#Name: Isong Mbah
#Date: Thu Jul 24 2022
#Project: To practice writing, planning, defining, calling functions, and using Python sequence, decision, repetition statements and lists.

import random

def getNumber():
    input_value = int(input("How many numbers per list: "))
    if input_value <= 0:
        print("Invalid input")
        
    else:
        return input_value

def generateList(input_value):
    my_list = random.sample(range(1, 10), input_value)
    return my_list

def addList(list1, list2):
    new_list = []
    for item in range(len(list1)):
        my_sum = list1[item] + list2[item]
        new_list.append(my_sum)
    return new_list

def multiplyList(list1, list2):
    new_list = []
    for item in range(len(list1)):
        multiple = list1[item] * list2[item]
        new_list.append(multiple)
    return new_list

def displayList(prompt, final_list):
    print(f"{prompt:^20}: {final_list}")

def main():
    my_value = getNumber()
    list1 = generateList(my_value)
    list2 = generateList(my_value)
    added_list = addList(list1, list2)
    multiplicated_list = multiplyList(list1, list2)
    counter = 0
    while counter < 4:
        counter  = counter + 1
        prompt = input()
        if prompt == "List 1":
            final_list = list1
            if not final_list:
                print("List is empty")
            displayList(prompt, final_list)
        elif prompt == "List 2":
            final_list = list2
            if not final_list:
                print("List is empty")
            displayList(prompt, final_list)
        elif prompt == "Added List":
            final_list = added_list
            if not final_list:
                print("List is empty")
            displayList(prompt, final_list)
        elif prompt == "Multiplied List":
            final_list = multiplicated_list
            if not final_list:
                print("List is empty")
            displayList(prompt, final_list)

if __name__ == "__main__":
    main()