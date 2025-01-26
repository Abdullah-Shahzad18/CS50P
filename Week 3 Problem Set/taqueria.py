menu = {
    "Baja Taco" : 4.25,
    "Burrito" : 7.50,
    "Bowl" : 8.50,
    "Nachos" : 11.00,
    "Quesadilla" : 8.50,
    "Super Burrito" : 8.50,
    "Super Quesadilla" : 9.50,
    "Taco" : 3.00,
    "Tortilla Salad" : 8.00
}
sum = float(0)
while True:
    try:
        x = input("Item: ").title().strip()
        if x in menu:
            sum=sum+menu[x]
            print(f"\nTotal: ${sum:.2f}")
    except EOFError:
        print(f"\nTotal: ${sum:.2f}")
        break
    except KeyError:
        pass