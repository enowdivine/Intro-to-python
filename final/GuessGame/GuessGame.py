#NAME: ISONG MBAH
#DATE: WED JUL 27 2022
#PROJECT: CREATING A GUESSING GAME THAT CONTINUALLY ASK THE USER TO GUESS A NUMBER UNTILL THEY GET THE CORRECT NUMBER

#IMPORTING THE RANDOM FUNCTION
import random

#FUNCTION REQUESTING THE NAME OF THE PLAYER
def get_player_name():
    player_name = input("Please enter your name: ")
    return player_name

#FUNCTION THAT STORES THE NAME OF THE PLAYER IN THE HISTORY FILE
def store_name(player_name, guess_count):
    store_file = open('history.txt', 'a')
    store_file.write(f"{player_name}\n")
    store_file.write(f"{str(guess_count)}\n")
    store_file.close()

#FUNCTION TO READ ALL PLAYER NAMES AND GUESS COUNTS IN HISTORY FILE
def read_history():
    history_file = open('history.txt', 'r')
    Lines = history_file.readlines()

    all_players = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
    
    #DIVIDING THE PLAYERS ARRAY INTO GROUPS OF 2
    single_player = all_players(Lines, 2)

    counter = 0
    for counter in range(len(single_player)):
        game_history_name = single_player[counter][0]
        game_history_guesses = single_player[counter][1]

        #PRINTING THE PLAYER NAME AND THE GUESS COUNT FOR EACH PLAYER
        print(f"{game_history_name}                                  {game_history_guesses}")
    
#FUNCTION TO DISPLAY THE HEADER THE SCORES
def display_score():
    print(f"Name                           Guesses")
    print(f"______________________________________")

    #CALLING THE read_history FUNCTION THAT READS ALL THE PLAYER NAMES AND GUESS COUNTS AND LIST THEM
    read_history()

#FUNCTION ASKING THE USER TO PLAY AGAIN OR QUIT THE GAME
def repeat_game():
    flag = True
    while flag:

        #INPUT RESPONSE FROM THE USER TO CONTINUE PLAYING OR NOT
        player_response = input("Would you like to play again (y/n)?: ")
        if player_response == 'y':
            return True
        elif player_response == "n":
            return False
        if player_response == 'Y':
            return True
        elif player_response == "N":
            return False
        else: 
            print("Not a valid entry (Y/y or N/n)")
        
#THE MAIN FUNCTION WHERE THE PROGRAM STARTS AND CALL ALL THE OTHER FUNCTIONS
def main():
    #CALLING THE DISPLAY_SCORE FUNCTION
    display_score()
    #CALLING THE FUNCTION THAT GET THE NAME OF THE USER
    player_name = get_player_name()
    outer_loop = True
    while outer_loop:
        flag = True

        #GENERATING THE RANDOM NUMBER FOR THE USER TO GUESS
        guess_integer = random.randint(1, 100)
        guess_count = 0

        #WHILE LOOP THAT CONTINUALLY ASK THE USER FOR THE CORRECT GUESS
        while flag: 
            guess_input = input("Guess an integer between 1 and 100: ")
            if guess_input.isdigit():
                guess_count += 1
                if  int(guess_input) > guess_integer:
                    print("Your guess is too high")
                elif  int(guess_input) < guess_integer:
                    print("Your guess is too low")
                elif  int(guess_input) == guess_integer:
                    print("Congratulations - your are right!")
                    store_name(player_name, guess_count)
                    flag = False
            else: print("Input is not an integer")

        #CALLING THE REPEAT_GAME FUNCTION WHICH RETURNS A BOOLEAN
        player_response = repeat_game()

        #CONDITIONS CHECKING THE RESPONSE FROM THE REPEAT_GAME FUNCTION
        if player_response == True:
            flag = True
        elif player_response == False:
            outer_loop = False

if __name__ == "__main__":
    main()