#print "guess a number between 1-100"
#user inputs number 
#checks if the input is above or below 
#hint too high or too low
#count after how many try user guessed correctly 
#Congratualte & indicate count.

import random




number_to_guess = random.randint(1,10)
count = 0


while True:
    try:
        user_guessed_string = input('guess natural number betweeen 1 - 10: ')
        user_guessed_number = int(user_guessed_string)
            
        if user_guessed_number == number_to_guess:
            print (f'congratutations you guessed the number after {count+1} try')
            break
        elif user_guessed_number > number_to_guess:
            print('too high! try again')
            count += 1

        elif user_guessed_number < number_to_guess:
            print('too low! try again')
            count +=1
    except ValueError:
        print ('Enter a valid number')
    

  

    





