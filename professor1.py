import random
import sys


def get_level():

    while True:
        random_int_list = []
        try: 
            level = int(input('Level:'))
            if 0 < level < 4:
                print(str(generate_integer(level)))
                i = 20
                while i > 0:
                    gen_int = generate_integer(level)
                    print(gen_int)
                    random_int_list.append(gen_int)
                    i = i - 1

                print(random_int_list)
                #Note: 07/19/23: try generating a 20 int random list and then slicing out the even and odd indexes into x an y
                continue
            else:
                print('Invalid level_ inside try')
                continue
            

    
        except ValueError:
            print('Invalid level')
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



get_level()


