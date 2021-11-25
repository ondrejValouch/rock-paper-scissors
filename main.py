import random

users_choice = input('Make your choice: rock, paper, scissors: ')
number = random.randint(0,3)

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

#Write your code below this line 👇

if number == 0 and users_choice == 'rock':
  print(rock)
  print(rock)
  print('Draw')
elif number == 0 and users_choice == 'paper':
  print(rock)
  print(paper)
  print('You Won!')
elif number == 0 and users_choice == 'scissors':
  print(rock)
  print(scissors)
  print('You Lost!')
elif number == 1 and users_choice == 'rock':
  print(paper)
  print(rock)
  print('You Lost!')
elif number == 1 and users_choice == 'paper':
  print(paper)
  print(paper)
  print('Draw')
elif number == 1 and users_choice == 'scissors':
  print(paper)
  print(scissors)
  print('You Won')
elif number == 2 and users_choice == 'rock':
  print(scissors)
  print(rock)
  print('You Won')
elif number == 2 and users_choice == 'paper':
  print(scissors)
  print(paper)
  print('You Lost')
elif number == 2 and users_choice == 'scissors':
  print(scissors)
  print(scissors)
  print('Draw')
else:
  print('invalid values')  
