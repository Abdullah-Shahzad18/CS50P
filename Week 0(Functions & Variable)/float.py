x = input("Enter x in decimal number")
y = input("Enter y in decimal number") 

# z = round(float(x) + float(y)) 
z = float(x) + float (y)
# print(z)
#to format an integer in international format
print(f"{z:,}")
print(f"{z:.2f}")