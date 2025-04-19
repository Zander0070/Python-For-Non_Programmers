import random

num = random.randint(1,10)
num2 = random.randint(0,2)

fortune = ["you will be married at age : ", "your lucky number is : ", "Yoyu will win the lotto at age : "]

print(f'{fortune[num2]} {num}' )