greet = input("Greetings: ").lower().strip()


if greet.startswith("hello")==True:
    print("$0")
elif greet.startswith("h")==True and greet!="hello":
    print("$20")
else:
    print("$100")


     

