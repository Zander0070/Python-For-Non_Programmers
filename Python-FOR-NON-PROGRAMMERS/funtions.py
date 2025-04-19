def Hello(names):
    print(f"hello {names}")

Hello("Steve")

def AddNums(num1,num2):
    total = 0
    total = num1 + num2
    print(f"Your total is {total}")


AddNums(12,222)


def DogInfo(age,name):
    
    if age < 1:
        print(f"This is {name} he is {age} years old he is still a puppy")
    else:
         print(f"This is {name} he is {age} years old he is a grown dog")
    


DogInfo(0,"stevie")