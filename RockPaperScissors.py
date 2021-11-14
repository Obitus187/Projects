import random

# test

def computer_turn():  # Generates computer's choice
    computer_list = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(computer_list)
    return computer_choice


def intro():  # Start of the games!
    playgame = input('Hello, would you like to play a game? (yes/no)\n')  # Asks for players input
    turns_played = 1  # Keeps track of turns
    player_score = 0  # Keeps track of player score
    comp_score = 0  # Keeps track of computer score
    if playgame == 'yes':  # If player wants to play, goes to while loop
        best_of = input('How many games would you like to play?\n')  # asks how many turns to play
        while int(best_of) + 1 > int(
                turns_played):  # Takes best of (plus 1 since python starts at 0) and loops till turns match best_of
            # (inputed turns user wants to play)
            print('Turn number ' + str(turns_played))  # Keeps track of the turns
            p_choice = input(
                'Which will it be? Rock, Paper or Scissors?\n')  # Player picks their option (No built in protection
            # if they answer wrong)
            c_choice = str(computer_turn())  # Pulls a random choice from definition computer_turn
            turns_played += 1 # adds to turns played after every iteration of the loop
            print('Computer picks ' + str(c_choice))  # Let's the player know what the computer picked
            if str(c_choice) == str(p_choice):  # If they pick the same thing it's a tie and moves to next round
                print('Tie round!')
            elif str(p_choice) == 'Rock':  # If player picks rock, checks computers choice and returns a win or lose
                if str(c_choice) == 'Paper':
                    print('Paper beats Rock!')
                    comp_score += 1
                    print('Computer score: ' + str(comp_score), '   Player score: ' + str(player_score))
                elif str(c_choice) == 'Scissors':
                    print('Rock beats Scissors!')
                    player_score += 1
                    print('Computer score: ' + str(comp_score), '   Player score: ' + str(player_score))
            elif p_choice == 'Paper':  # If player picks paper, checks computers choice and returns a win or lose
                if c_choice == 'Scissors':
                    print('Scissors beats Paper!')
                    comp_score += 1
                    print('Computer score: ' + str(comp_score), '   Player score: ' + str(player_score))
                elif c_choice == 'Rock':
                    print('Paper beats Rock!')
                    player_score += 1
                    print('Computer score: ' + str(comp_score), '   Player score: ' + str(player_score))
            elif p_choice == 'Scissors':  # If player picks scissors, checks computers choice and returns a win or lose
                if c_choice == 'Rock':
                    print('Rock beats Paper!')
                    comp_score += 1
                    print('Computer score: ' + str(comp_score), '   Player score: ' + str(player_score))
                elif c_choice == 'Paper':
                    print('Scissors beats paper')
                    player_score += 1
                    print('Computer score: ' + str(comp_score), '   Player score: ' + str(player_score))
            else:
                print('Please pick a valid choice')  # if they don't pick Rock, Paper, or Scissors it tells them to pick
                # A valid choice
        else:  # Once loop ends, provides end game results and if they want to rematch, loop intro again.
            if player_score == comp_score:
                print('Tie game! No body wins...')
                regame = input('Play again? (yes/no)\n')
                if regame == 'yes':
                    intro()
                else:
                    return
            elif player_score > comp_score:
                print('Congratulations! You beat the computer!')
                regame = input('Play again? (yes/no)\n')
                if regame == 'yes':
                    intro()
                else:
                    return
            else:
                print('You lose.')
                regame = input('Play again? (yes/no)\n')
                if regame == 'yes':
                    intro()
                else:
                    return

    elif playgame == 'no':  # if player doesn't want to play
        print('Have a nice day!')
    else:  # Loops back to intro if they don't pick yes or no
        print('Not a valid choice')
        return intro()


intro()  # initiates the game
