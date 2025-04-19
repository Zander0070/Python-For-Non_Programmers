total = 0
numbers = [62, 66, 94, 97, 25, 11, 68, 54, 48, 67]

for I in range(10):
    if numbers[I] % 2 == 0:
        total = total + numbers[I]
        if I > 0:
            print(total)

        