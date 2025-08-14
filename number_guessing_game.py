#print "guess a number between 1-100"
#user inputs number 
#checks if the input is above or below 
#hint too high or too low
#count after how many try user guessed correctly 
#Congratualte & indicate count.

import random




number = random.randint(1,10)

count = 0

while True:
    userGuessStr= input('guess natural number betweeen 1 - 10: ')
    userGuess = int(userGuessStr)
    if not (1<= userGuess <=10):
        print ('invalid number!') 
        
    elif userGuess == number:
        print (f'congratutations you guessed the number on your {count+1} try')
        
    elif userGuess > number:
        print('too high! try again')
        count += 1

    elif userGuess < number:
        print('too low! try again')
        count +=1
    
    else:print ('invalid number')
    break

  

    





