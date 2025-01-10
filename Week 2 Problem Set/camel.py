word = input("camelCase: ")
print("snake_case: ",end="")
for s in word:
    if s.isupper()==True:
      string = print("_",s.lower(),end="",sep="")
    else:
       string = print(s,end="")
       
       
    
    
