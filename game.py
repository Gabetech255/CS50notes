import random
import sys


def main():
    while True:
        try: 
            user_in = int(input("Level: "))

            
            # This checks if the int is positive and will either move to the next step or use continue to finish the try and re-loop
            if user_in >= 1:
                
                    #randrange generates my random number and use var + 1 to include the var in the range 
                random_number = random.randrange(1, user_in + 1)
                    #converts to a int for easy comparison
                random_number = int(random_number)
                # Troubleshoot random number - print('random: ' + str(random_number))
                while True:
                    guess = int(input('Guess: '))
                
                    if guess < random_number:
                        print("Too small!")
                        continue
                    if guess > random_number:
                        print('Too large!')
                        continue
                    else: 
                        print('Just right')
                        sys.exit()
                
            else:
                
                continue
            
            #this brings us back to the begining of the while loop and prompts if user enters anything other than an Integer
        except ValueError:
            continue



main()


