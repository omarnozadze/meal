def main():
    time = convert(input("What time is it?"))
    if 7 <= time <= 8:
        print("breakfeast time")
    elif 12 <= time <= 13:
        print("dinner time")
    elif 18 <= time <= 19:
        print("supper time")
    else:
        print("Not meal time")
            
def convert(time):
    hours,minutes=time.split(":")
    time=float(minutes)/60
    return float(hours)+time 


main()     