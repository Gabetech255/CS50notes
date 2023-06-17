def main():
    time = input("What time is it?  ")
    # return value will be put into time as a float 
    time = convert(time)
    
    if  7.0 <= time <= 8.0:
        print("breakfast time")

    elif 12.0 <= time <= 13.0:
        print("lunch time")

    elif 18.0 <= time <= 19.0:
        print("dinner time")



def convert(t):
    hours, minutes = t.split(":")
    hours = float(hours)
    minutes = float(minutes)
    hoursASfloat = (hours + (minutes /60 ))
    return hoursASfloat


if __name__ == "__main__":
    main()

