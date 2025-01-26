while True:
    try:
        frac = input("Fraction: ")
        numerator,denominator = frac.split("/")
        numerator=int(numerator)
        denominator=int(denominator)
        quotient=float(numerator/denominator)
        if quotient==0:
            print("E")
            break
        elif quotient==1:
            print("F")
            break
        elif quotient<0.10:
            print("E")
            break
        elif 0.90<quotient and quotient<1:
            print("F")
            break
        elif quotient<1:
            print(int(round((numerator/denominator)*100)),"%",sep="")
            break
        elif quotient>1:
            continue
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

