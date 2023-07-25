import requests
import json
import sys

#sys argv creates an array where [0] is the name of the file and each index after is deliniated by a space | arguments are passed as strings

try:
    
    # stop on index error meaning nothing was entered as the argument 
    try:

        argument_check = sys.argv[1]
        # stop on value error meaning there was an argument passed but it was not a number and couldnt be converted to a float 
        try:
            bitcoin = float(argument_check)
            url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
            response = requests.get(url)
            #passes the json response as a dictionary 
            price_index = response.json()
            # this digs into the nested dictionary and recovers the value from the key rate_float
            bitcoin_value = price_index['bpi']['USD']['rate_float']
            amount = bitcoin * bitcoin_value
            print(f'${amount:,.4f}')
            

            sys.exit()
            
        except ValueError:
            print('Command-line argument is not a number')
            sys.exit()
            

    except IndexError:
        print('Missing command-line argument')
        sys.exit()

        
except requests.RequestException:
    print('Request exeption triggered')
    sys.exit()
