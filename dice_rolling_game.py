

#Ask user: do you want to roll the dice?
#  If the user enters y,
#    generate two random numbers.
#    print them 
#. If the user enters n,
#     Print thank you message
#     terminate 
#  Else 
    #   Print invalid choice 

# loop infinitely as long as user want to play

print('Dice Rolling game (die1, die2) !' )

import random

 
while True:
    choice = input ('do you want to play y/n: ').lower()
    if choice == 'y':
        die1 = random.randint(1,6) 
        die2 = random.randint(1,6)  
        print (f'You rolled: ({die1}, {die2})')

    elif choice == 'n':
        print('Thanks for playing')
        break 
    else: 
        print('Invalid choice!') 
