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

import random

RPS_list = [rock, paper, scissors]
computer_do = random.randint(0,2)
print('''input you choice:
 1 - rock 
 2 - paper
 3 - scissors
 ''')
user_do = int(input())
user_do -= 1
print('You choice is:')
print(RPS_list[user_do])
print('Computer choice is:')
print(RPS_list[computer_do])
if (user_do - computer_do) == -2 or (user_do - computer_do) == 1:
  print('You win')
elif user_do == computer_do:
  print('Nobody win')
else:
  print('Computer win')








