import random

A = "Rock"
B = "Paper"
C = "Scissors"
choices = [0, 0]
total_wins = []
player_name = []


def start_game():
    print("Welcome to Rock Paper Scissors: Would you like to play?")
    print("Y = Begin Game")
    print("N = End Game")
    begin_answer = input("Select Y or N: \n")
    begin_answer = begin_answer.capitalize()
    if begin_answer == 'Y':
        player_name.append(input("What is your name?"))
        player_name[0] = player_name[0].title()
        player_choose()
    else:
        print("Thank You For Playing!")


def player_choose():
    print("Please Select Rock, Paper or Scissors")
    user_pick = int(input("1 = Rock, 2 = Paper, 3 = Scissors: "))
    choices[0] = user_pick
    if choices[0] == 1:
        print('You chose', A, "\n")
        computer_pick()
    elif choices[0] == 2:
        print('You chose', B, "\n")
        computer_pick()
    elif choices[0] == 3:
        print('You chose', C, "\n")
        computer_pick()
    else:
        print("Error Incorrect Letter\n")
        choices.pop()
        player_choose()


def computer_pick():
    rand_num = random.randint(1, 3)
    choices[1] = rand_num
    if rand_num == 1:
        print('Computer chose', A, "\n")
        choose_decision()
    elif rand_num == 2:
        print('Computer chose', B, "\n")
        choose_decision()
    else:
        print('Computer chose', C, "\n")
        choose_decision()


def choose_decision():
    if choices[0] == choices[1]:
        print("No winner, tie game!\n")
        tie_game()
    elif choices[0] == 1 and choices[1] == 3:
        print(player_name[0], "Wins!\n")
        player_wins()
    elif choices[0] == 2 and choices[1] == 1:
        print(player_name[0], "Wins!\n")
        player_wins()
    elif choices[0] == 3 and choices[1] == 2:
        print(player_name[0], "Wins!\n")
        player_wins()
    else:
        print("Computer Wins!\n")
        computer_wins()


def player_wins():
    total_wins.append([1, 0])
    play_again()


def computer_wins():
    total_wins.append([0, 2])
    play_again()


def tie_game():
    total_wins.append([0, 0])
    play_again()


def play_again():
    print('Would you like to play again?')
    play_again_answer = input("Select Y or N: \n")
    play_again_answer = play_again_answer.capitalize()
    if play_again_answer == 'Y':
        player_choose()
    else:
        print("Total Games Played: ", len(total_wins))
        total_score()


def total_score():
    player_wins = 0
    computer_wins = 0
    tie_games = 0
    for i in range(len(total_wins)):
        counter = 0
        for j in range(len(total_wins[i])):
            counter += (total_wins[i][j])
        if counter == 1:
            player_wins += 1
        elif counter == 2:
            computer_wins += 1
        elif counter == 0:
            tie_games += 1
    print(player_name[0], "won: ", player_wins, "games.")
    print("Computer won: ", computer_wins, "games.")
    print("Tie Games: ", tie_games, "games.")
    print("Thank you for playing!")

# change to have the possibility to play against another person
# slow down text so it outputs slower
