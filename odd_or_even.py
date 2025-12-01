with open("input.txt", "r") as input:
    for line in input:
        number = line.strip()
        number2 = int(number)

        if number2 % 2 == 0:
            print("even")
        else:
            print("odd")

