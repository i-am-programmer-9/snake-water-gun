import random
import os
import time
try:
    chance = int(input("Write how many times you'd want to play in a round: "))
    hm_pt = 0
    cmp_pt = 0
    i = 0
    def print_win(what_to):
        global hm_pt, cmp_pt, i
        if what_to == 0:
            hm_pt += 1
            print(f"\nGreat! You got a point. {i + 1} chances out of {chance} ")
        elif what_to == 1:
            print(f"\nOops! You lose this time. {i + 1} chances out of {chance} ")
            cmp_pt += 1
        elif what_to == 2:
            print(f"\nThat was a Tie, {i + 1} chances out of {chance}")
        print(f"\nYour Points: {hm_pt}\nComputer's Point: {cmp_pt}")
        i += 1
        time.sleep(5)
        os.system('cls')

    while i < chance:
        human_choice = input("\nChoose\ng/G for gun\nw/W for water\ns/S for snake: ")
        computer_choice = random.randint(0, 3)
        if computer_choice == 0:
            computer_choice = "Snake"
        elif computer_choice == 1:
            computer_choice = "Gun"
        else:
            computer_choice = "Water"
        # Snake will win over water
        # Gun will win over snake
        # Water will over gun
        print(f"\nComputer guessed {computer_choice}")
        if human_choice.lower() == 'g':
            if computer_choice == 'Snake':
                print_win(0)
            elif computer_choice == 'Water':
                print_win(1)
            else:
                print_win(2)
                
        elif human_choice.lower() == 's':
            if computer_choice == 'Water':
                print_win(0)
            elif computer_choice == 'Gun':
                print_win(1)
            else:
                print_win(2)
                
        elif human_choice.lower() == 'w':
            if computer_choice == 'Gun':
                print_win(0)
            elif computer_choice == 'Snake':
                print_win(1)
            else:
                print_win(2)
        else:
            print("That was wrong input busta, give as directed")

    if hm_pt > cmp_pt:
        print("\nCongrats! You won over computer")
    elif hm_pt < cmp_pt:
        print("\nOh No! You lose")
    else:
        print("\nMatch Tied")

except ValueError:
    print("You entered wrong input when I asked chances: ")
except:
    print("Something unknown happened")

