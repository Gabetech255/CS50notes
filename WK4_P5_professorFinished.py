import random
import sys


def main():

    while True:
        random_int_list = []
        try: 
            level = int(input('Level:'))
            if 0 < level < 4:
                #print(str(generate_integer(level)))
                i = 20
                while i > 0:
                    gen_int = generate_integer(level)
                    #print(gen_int)
                    random_int_list.append(gen_int)
                    i = i - 1

                
                #print(random_int_list)

                # Init A variables
                a_counter = 0
                x = 0
                y = 1
                answer_list = []
                x_list = []
                y_list = []

                # Generates list for print
                while a_counter < 10:
                    #print(random_int_list[x])
                    x_int = random_int_list[x]
                    x_list.append(x_int)
                    
                    #print(random_int_list[y])
                    y_int = random_int_list[y]
                    y_list.append(y_int)
                    
                    z_int = x_int + y_int

                    

                    answer_list.append(z_int)
                

                    #iterate variables
                    x = x + 2
                    y = y + 2
                    a_counter = a_counter + 1
                
                #Troubleshooot: print('x_list: ' + str(x_list))
                #Troubleshooot: print('y_list: ' + str(y_list))
                #Troubleshooot: print('answer list: ' + str(answer_list))
                
                #Initialize B variables  
                b_counter = 0
                x = 0
                y = 1
                Correct_Flag = 0
                user_score = 0
            
                wrong_counter = 0


                # prints and prompts Note[07/21/23]: this prompts each question and ends after all problems displayed add score functionallity
                while b_counter < 10:
                    x_in = x_list[b_counter]
                    y_in = y_list[b_counter]
                    user_answer = int(input(str(x_in) + ' + ' + str(y_in) + ' = : '))
                    z = x_in + y_in
                    #print('z = ' + str(z))

                    if user_answer == z:
                        Correct_Flag = Correct_Flag + 1
                        user_score = user_score + 1

                    elif user_answer != z and wrong_counter == 2:
                        print(str(x_in) + ' + ' + str(y_in) + ' = ' + str(z))
                        Correct_Flag = Correct_Flag + 1

                    else:
                        print('EEE')
                        wrong_counter = wrong_counter + 1
                        
                        
                    #iterate variables
                    if Correct_Flag == 1:
                        x = x + 2
                        y = y + 2
                        b_counter = b_counter + 1
                        Correct_Flag = Correct_Flag - 1
                        wrong_counter = 0

                    if b_counter == 10:
                        print('Score: ' + str(user_score))
                        sys.exit()
                        

                #Note: 07/19/23: try generating a 20 int random list and then slicing out the even and odd indexes into x an y
                continue
            else:
                #print('Invalid level')
                continue
            

    
        except ValueError:
            #print('Invalid level')
            continue

    # use the level var to determine the number of digits each randomly generated int will have 
def generate_integer(level):
    
    if level == 1: 
        
        gen_int = random.randint(1, 9)
        return gen_int
    
    elif level == 2:
        gen_int = random.randint(10, 99)
        return gen_int
        
    elif level == 3:
        gen_int = random.randint(100,999)
        return gen_int



main()


