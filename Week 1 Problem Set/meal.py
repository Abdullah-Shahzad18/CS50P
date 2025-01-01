def main():
        input_time = input("What time is it? ")
        formatted_time=convert(input_time)
        if 7.00 <= formatted_time <= 8.00:
            print("breakfast time")
        elif 12.00 <= formatted_time <= 13.00:
            print("lunch time")
        elif 18.00 <= formatted_time <= 19.00:
            print("dinner time")
        else:
            print("")
def convert(time):
    hr, min =time.split(":")
    minutes = float(min)/60
    hour = float(hr)
    time = hour + minutes
    return float(time)


if __name__ == "__main__":
    main()
