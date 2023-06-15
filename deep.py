def main():
    userIn = input("What is the answer to life, the universe, and everything?  ")
    userIn = userIn.strip()
    
    if userIn.lower() == '42':
        print('Yes')
    elif userIn.lower() == 'forty-two':
        print('Yes')
    elif userIn.lower() == 'forty two':
        print('Yes')
    else:
        print('No')

main()