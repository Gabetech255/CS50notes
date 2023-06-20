userin = input("input camel case  ")
result = ''
count = 0 

for letter in userin:
    if count == 0:
        result += letter.lower()
    

    elif letter == letter.lower():
        result += letter
    

    elif letter != letter.lower():
        result += '_'
        result += letter.lower()
        
    count += 1


print(result)
