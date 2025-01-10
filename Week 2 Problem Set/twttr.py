string =  input("Input: ")
print("Outpu: ",end="")
for s in string:
    if s in ["A","E","I","O","U","a","e","i","o","u"]:
        continue
    print(s,end="",sep="")
