# x = int(input())
# y = int(input())


# # if x>y:
# #     print("x is greater than y")
# # elif x<y:
# #     print("x is lesser thsn y")
# # else:
# #     print("x is equal to y")

# if x>y or x<y:
#     print("x is not equal y")    
name = input ("Enter your favourite team")


match name:
    case "Babar":
        print("56")
    case "Kohli":
        print("18")
    case "Shaheen Afridi":
        print("10")
    case _:
        print("Player is not recognized")