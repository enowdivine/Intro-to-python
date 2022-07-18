#Name: Isong Mbah
#Date: Thu Jul 18 2022
#Project: Reading golfers scores from a text file and displaying  their average scores

import os
from os import path

# functiion to get the file name
def getFileName():
    file_name = input("Enter file to read: ")
    return file_name

# function header of output data
def displayHeader():
    print("Golfer                       score")
    print("___________________________________")


# function to display output data
def displayData(golfer_name, average_score):
    print(f'{golfer_name}                              {average_score}')

# funtion to process file
def openReadFile(file_name):
    # checking if the file exist
    file_exists = path.exists(file_name)
    if file_exists:
        # checking if the file is empty
        if os.stat(file_name).st_size == 0:
            print("File is empty")
        else:

            my_file = open(file_name, 'r')
            Lines = my_file.readlines()

            all_arrays = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
            # splitting array in goups of 5
            sub_arrays = all_arrays(Lines, 5)

            # calling the header fumction
            displayHeader()

            counter = 0
            for counter in range(len(sub_arrays)):
                golfer_name = sub_arrays[counter][0]
                sum = int(sub_arrays[counter][1]) + int(sub_arrays[counter][2]) + int(sub_arrays[counter][3]) + int(sub_arrays[counter][4])
                average_score = sum / 4

                # calling the displayData function
                displayData(golfer_name, int(average_score))    
    else:
        print("File does not exist")


# main function
def main():
    file_name = getFileName()
    openReadFile(file_name)

if __name__ == "__main__":
    main()