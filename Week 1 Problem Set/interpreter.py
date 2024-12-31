x, y, z = input("Expression: ").split()


match y:
    case "+":
        sum = float(x) + float(z)
        print(f"{sum:.1f}")
    case "-":
        subtract = float(x) - float(z) 
        print(f"{subtract:.1f}")
    case "/":
        if y!=0:
            division = float(x) / float(z) 
            print(f"{division:.1f}")
        else:
            print("Math Error")
    case  "*":
        product = float(x) * float(z)
        print(f"{product:.1f}")
    case _: 
        print("INVALID OPERATOR (+,-,/,*)")                    


