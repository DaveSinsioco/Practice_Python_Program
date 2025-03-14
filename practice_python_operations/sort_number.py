# creating a loop

start = "y"
while start == "y":
    
# ask them the choose program

    program = int(input("Program(1-5)? "))

    # Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

    if program == 1:
        num_counter = 0
        numbers = []
        for num in range(10):
            num_counter += 1
            num = int(input(f"Number #{num_counter}? "))
            numbers.append(num)

        # Make individual numbers unique to 1 copy
        unique_numbers = [num for num in numbers if numbers.count(num) == 1]
        print (unique_numbers)        

    # Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
    
    if program == 2:
        num_counter = 0
        numbers = []
        for num in range(10):
            num_counter += 1
            num = int(input(f"Number #{num_counter}? "))
            numbers.append(num)

        unique_numbers = []

        # remove duplicates

        for num in numbers:
            if num not in unique_numbers:
                unique_numbers.append(num)

        print(unique_numbers)

    # Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate. 
    
    if program == 3:
        numbers = []
        while True:
            try:
                while True:
                    num = int(input("Number? "))
                    if num in numbers:
                        print("Duplicate")
                    else:
                        print("Unique")
                        numbers.append(num)
            except ValueError:
                break