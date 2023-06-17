def main ():
    exp = input("What do you want to calculate?  ")
    
    x, y, z = exp.split(" ")
    x = int(x)
    z = int(z)
    expout = 0

    if y == '+':
        expout = float(x + z)
        print(expout)

    elif y == '-':
        expout = float(x - z)
        print(expout)

    elif y == '*':
        expout = float(x * z)
        print(expout)

    elif y == '/' and z != 0:
        expout = float(x / z)
        print(expout)
    
    elif z == 0:
        print('divide by zero error')
    
    else:
        print('Not a valid expression')




main()