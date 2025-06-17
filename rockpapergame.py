import random
rock= '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
 
'''
paper=''' 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)


'''

scissors=''' 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)


'''

game = [rock,paper,scissors]

choice = int(input('\n what would do like to choose !! 0 for ROCK, 1 for PAPER, 2 for SCISSORS : '))
print('YOU CHOSE')
print(choice)



computer = random.randint(0,2)
print('COMPUTER CHOSE:')
print(computer)


