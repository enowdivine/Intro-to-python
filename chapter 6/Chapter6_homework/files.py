#Name: Isong Mbah
#Date: Thu Jul 11 2022
#Project: Reading file content and writting the content on another file.

import os
from os import path

# writting to the output file function
def writeLine(Lines):
    # using write function
    output_file = open('output.txt', "w")
    count = 0
    for line in Lines:
        count += 1
        output_file.write(str(count) + ': ' + line)
    output_file.close()


# readind lines from file function
def readLine(file_name):

    # Using readlines()
    my_file = open(file_name, 'r')
    Lines = my_file.readlines()
    writeLine(Lines)

def main():

    flag = True

    while flag:
        # getting file name
        file_name = input("Enter filename: ")

        # checking if the user enters the quit command
        if(file_name == "quit"):
           flag = False
        else:
            # checking if the file exist
            file_exists = path.exists(file_name)
            if file_exists:
                # checking if the file is empty
                if os.stat(file_name).st_size == 0:
                    print("File is empty")
                else:
                    # calling the readline function
                    readLine(file_name)
            else:
                print("File does not exist")

if __name__ == "__main__":
    main()

    

