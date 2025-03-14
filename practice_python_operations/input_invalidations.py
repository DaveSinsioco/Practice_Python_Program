# creating a loop

start = "y"
while start == "y":
    
# ask them the choose program

    program = int(input("Program(1-5)? "))

    # Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

    if program == 1:
        num_counter = 0
        numbers = []
        for num in range(10):
            num_counter += 1
            num = int(input(f"Number #{num_counter}? "))
            numbers.append(num)

        # Make the numbers with copy show
        duplicate_numbers = [num for num in numbers if numbers.count(num) > 1]
        print (duplicate_numbers)

    # Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

    if program == 2:
        numbers = []
        while True:
            try:
                while True:
                    num = int(input("Number? "))
                    numbers.append(num)
            except ValueError:
                break

        # Display the number with the most number of duplicate.

        duplicate_numbers = [num for num in numbers if numbers.count(num) > 1]
        print (max(set(duplicate_numbers), key=duplicate_numbers.count))