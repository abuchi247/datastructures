import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

selections = [rock, paper, scissors]


def display_result(human, computer):
    # RULES
    # Rock wins against scissors
    # Scissors wins against paper
    # Paper wins against rock


    print(selections[human])
    print("Computer chose:")
    print(selections[computer])

    if human == 0 and computer == 2:
        print("You win")
    elif computer == 0 and human == 2:
        print("You lose")
    elif human > computer:
        print("You win")
    elif computer > human:
        print("You lose")
    else:
        print("You drew")


def menu():
    num_test = 10
    t = 0

    while t < num_test:
        human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors\n"))
        while human_choice < 0 or human_choice > 2:
            print("Invalid entry")
            human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors\n"))

        computer_choice = random.randint(0, 2)
        display_result(human_choice, computer_choice)

        t += 1


if __name__ == "__main__":
    menu()
