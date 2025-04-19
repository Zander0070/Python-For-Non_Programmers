def Has_Remiander(num1,num2):
    total = 0
    total = num1 + num2

    if total % 2 == 0:
        return print (f"Please note that {num1} divided by {num2} has no remianders")
    elif total % 2 == 1:
        return print (f"Please note that {num1} divided by {num2} has remianders")
    

Input1 = input("Please enter our first number : " )
Input2 = input("Please enter your second number : ")

Has_Remiander(int(Input1), int(Input2))
