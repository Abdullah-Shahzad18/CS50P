name = input("Enter your name:").strip().title()
# #Remove white spaces between  string
# #There is a builtin fuction in  python to capatailize string

# # name = name.strip()
# # name = name.capitalize()
# # name =name.title()
# #another way to write this function in one line
# # name = name.strip().title()
# #This only capatalize the first letter
# #to capatalize the title like John Wick

#to split the name in to first and last name we use a funtion
first, last = name.split(" ")
print(f"Your first name  is {first}")
print(f"Your second name is {last}")


