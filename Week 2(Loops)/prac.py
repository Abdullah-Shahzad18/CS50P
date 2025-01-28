def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)>=1 and len(s)<=5:    
        if s[0:2].isalpha().upper() and check_number==True and check_punctuation==True:
            return True       

def check_number(s):
    for loop in s:
        if s[0:len(s)-2].isnumeric() or s[0:len(s)-2]==0:
            return False
        else:
            return True
def check_punctuation(s):
    for loop in s:
        if s.isalpha().isnumeric():
            return True
        else:
            return False

main()