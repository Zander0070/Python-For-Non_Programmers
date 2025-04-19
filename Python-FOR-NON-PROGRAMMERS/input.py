InputInfo = input("do you want to uppercase or lowercase ? ")
name = input("Plese enter your name : ")

if InputInfo == "uppercase":
    print(name.upper())
elif InputInfo == "lowercase":
    print(name.lower())
else:
    print("Please enter a valid option next time")