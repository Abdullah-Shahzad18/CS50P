
def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    
    if len(s) < 2 or len(s) > 6:
        return False
    
    if not s[0:2].isalpha():
        return False
    
    if not check_number(s):
        return False
    
    if not check_punctuation(s):
        return False
    return True


def check_number(s):
    number_started = False
    for i, char in enumerate(s):
        if char.isdigit():
            
            if not number_started:
                number_started = True
                if char == '0':  
                    return False
            elif not s[i:].isdigit():  
                return False
    return True


def check_punctuation(s):
    
    return s.isalnum()


main()
