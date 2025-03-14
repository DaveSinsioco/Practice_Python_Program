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