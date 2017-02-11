# 1. Introduce Game
# 2. Get user input (rock, paper, scissors)
# 3. Random computer output (rock, paper, scissors)
#     3a. Compare input & output: rock beats scissors, paper beats rock, scissors beats paper, or tie.
# 4. Indicate winner of round 1 (or tie).
# 5. Get user input (rock, paper, scissors)
# 6. Random computer output (rock, paper, scissors)
#     6a. Compare input & output: rock beats scissors, paper beats rock, scissors beats paper, or tie.
# 7. Indicate winner of round 3 (or tie; could be end of game)
# 8. Continue until someone wins 2/3 games (or consider best of 5 for longer games)
# Other Considerations:
# - Account for bad user input
# - Allow use to choose number of rounds

#Needs Tweaking:
# - Right now, ties don't count towards the score but still count in the number of games. Need to find a way to exclude them all together and keep going.
# - Line 135: figure out a way to get back to Y/N play question. Split intro() into 2 functions?
# - Make everything prettier when printed. Ascii Art?


import random
computer_list = ["rock", "paper", "scissors"]
player_score = []
computer_score = []

def intro():
    name = raw_input("\n" "What is your name?: ")
    play_choice = raw_input("\n" "Hello, %s! Would you like to play Rock, Paper Scissors? Y/N: " % (name))
    return play_choice

def game_play():
    player = raw_input("\n" "Shoot!: ")
    computer = random.choice(computer_list)
    print "\n" "Computer: ", computer
    if player == computer:
        print "\n" "Tie!"
    elif player != computer:
        if player == "rock":
            if player == "rock" and computer == "scissors":
                print "\n" "Rock beats scissors! :)"
                player_score.append(1)
            if player == "rock" and computer == "paper":
                print "\n" "Paper beats rock :("
                computer_score.append(1)
            if computer == "rock" and player == "scissors":
                print "\n" "Rock beats scissors :("
                computer_score.append(1)
        elif player == "paper":
            if player == "paper" and computer == "rock":
                print "\n" "Paper beats rock! :)"
                player_score.append(1)
            if player == "paper" and computer == "scissors":
                print "\n" "Scissors beats paper :("
                computer_score.append(1)
            if computer == "paper" and player == "rock":
                print "\n" "Paper beats rock :("
                computer_score.append(1)
        elif player == "scissors":
            if player == "scissors" and computer == "paper":
                print "\n" "Scissors beats paper! :)"
                player_score.append(1)
            if player == "scissors" and computer == "rock":
                print "\n" "Rock beats scissors :("
                computer_score.append(1)
            if computer == "scissors" and player == "paper":
                print "\n" "Scissors beats paper :("
                computer_score.append(1)
        else:
            print "Please enter 'rock', 'paper', or 'scissors'."

def play_again():
    while(True):
        answer = raw_input("\n" "Would you like to play again? Y/N: ")
        if answer == "Y":
            del player_score[:]
            del computer_score[:]
            num_of_games()
        if answer == "N":
            print "\n" "Have a great day!" "\n"
            break
        else:
            print "Please enter Y or N"

def game_final():
    if len(player_score) > len(computer_score):
        print "\n" "CONGRATULATIONS! You've won the game!"
    elif len(player_score) == len(computer_score):
        print "\n" "There is no winner."
    else:
        print "\n" "Game Over. You lose."

def num_of_games():
    while (True):
        games_num = raw_input("\n" "How many rounds would you like to play? (1, 3, 5, or 7?): ")
        if games_num == "1":
            game_play()
            game_final()
            play_again()
            break
        if games_num == "3":
            game_count = 0
            while game_count < 3:
                game_play()
                game_count = game_count + 1
            game_final()
            play_again()
            break
        if games_num == "5":
            game_count = 0
            while game_count < 5:
                game_play()
                game_count = game_count + 1
            game_final()
            play_again()
            break
        if games_num == "7":
            game_count = 0
            while game_count < 7:
                game_play()
                game_count = game_count + 1
            game_final()
            play_again()
            break
        if games_num != "1" or "3" or "5" or "7":
            print "Please enter 1, 3, 5, or 7"

def main():
    while(True):
        play_choice = intro()
        if play_choice.upper() == "Y":
            num_of_games()            
        elif play_choice.upper() == "N":
            print "\n" "You're missing out!" "\n"
            break
        else:
            print "\n" "Please enter Y or N" #makes you enter name again - figure out a way to get back to Y/N play question.
            main()
        break     

if __name__ == '__main__':
    main()






