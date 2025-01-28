# #exception is used to simplify error messages 
# # try:
# #     x = int(input("Enter a variable"))
# #     print(f"value of x is {x}")
# # except ValueError:
# #     print("x is not an integer")    
# # #valueerror refers to the incorrect datatye of input
# # Typo in variable name
# my_variable = 10
# print(my_varible)  # Raises NameError: name 'my_varible' is not defined
while True:
    try:
        x = int(input("Enter a value of x: "))
    except:
        print("x is not an integer")
    else:
        break

print(f"Value of x will be {x}")        



