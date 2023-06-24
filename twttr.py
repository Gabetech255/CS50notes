def main():
    UserIn = input('input message: ')
    UserIn = UserIn.lower()
    answer = check(UserIn)
    print(answer)

def check(UserIn):
    letterlist = []
    for letter in UserIn:
        letterlist.append(letter)
    lenlist = len(letterlist)

    print(lenlist)
    i = 0
    answer = ''

    for letter in letterlist:
        v = 0
        if letter == 'a':
            print('its an a')
            continue

        if letter == 'e':
            print('its an e')
            continue

        if letter == 'i':
            print('its an i')
            continue
            
        if letter == 'o':
            print('its an o')
            continue

        if letter == 'u':
            print('its a u')
            continue
        answer = answer + letter
    
    
    '''for letter in letterlist:
        answer = answer + letter
'''



    return answer
main()