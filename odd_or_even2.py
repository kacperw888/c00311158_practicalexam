with open("input.txt", "r") as input:
    for line in input:
        number = line.strip()
        number2 = int(number)
        number3 = str(number2)

        with open("output.md", "w") as output:        
            if number2 % 2 == 0:    
                output.write((number3 + " even"))
                print(number3 + " even")
            else:
                output.write((number3 + " odd"))
                print(number3 + " odd")

