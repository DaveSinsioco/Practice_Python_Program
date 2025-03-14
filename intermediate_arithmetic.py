# Creating a loop

start = "y"
while start == "y":
    
# asking which program

    program = int(input("Program(1-10)? "))
        
    # Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

    if program == 1:
        num1 = int(input("1st number? "))
        num2 = int(input("2nd number? "))
        if num1 < num2:
            print(num1)
        if num1 > num2:
            print(num2) 

    # Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

    if program == 2:
        num1 = int(input("1st number? "))
        num2 = int(input("2nd number? "))
        if num1 != num2:
            print("Not Equal")

    # Prog03: Create a program that ask user to input 2 numbers. Print the difference of the two numbers.

    if program == 3:
        num1 = int(input("1st number? "))
        num2 = int(input("2nd number? "))
        print(f"{num1 - num2}")

    # Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

    if program == 4:
        num1 = int(input("1st number? "))
        num2 = int(input("2nd number? "))
        print(f"{round(num1 / num2)}")

    # Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

    if program == 5:
        num1 = int(input("1st number? "))
        num2 = int(input("2nd number? "))
        print(f"{num1 % num2}")
        
    # Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

    if program == 6:
        num1 = int(input("1st number? "))
        num2 = int(input("2nd number? "))
        num3 = int(input("3rd number? "))
        num4 = int(input("4th number? "))
        num5 = int(input("5th number? "))
        num6 = int(input("6th number? "))
        num7 = int(input("7th number? "))
        num8 = int(input("8th number? "))
        num9 = int(input("9th number? "))
        num10 = int(input("10th number? "))
        print(f"{num1 - (num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10)}")
        
    # Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

    if program == 7:
        num1 = int(input("1st number? "))
        num2 = int(input("2nd number? "))
        num3 = int(input("3rd number? "))
        num4 = int(input("4th number? "))
        num5 = int(input("5th number? "))
        num6 = int(input("6th number? "))
        num7 = int(input("7th number? "))
        num8 = int(input("8th number? "))
        num9 = int(input("9th number? "))
        num10 = int(input("10th number? "))
        
    # Checks if number is odd
    
        even_counter = 0
        if num1 % 2 == 0:
            even_counter += 1
        if num2 % 2 == 0:
            even_counter += 1
        if num3 % 2 == 0:
            even_counter += 1    
        if num4 % 2 == 0:
            even_counter += 1
        if num5 % 2 == 0:
            even_counter += 1
        if num6 % 2 == 0:
            even_counter += 1
        if num7 % 2 == 0:
            even_counter += 1
        if num8 % 2 == 0:
            even_counter += 1
        if num9 % 2 == 0:
            even_counter += 1
        if num10 % 2 == 0:
            even_counter += 1
            
        print(even_counter)

    # Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)

    if program == 8:
        number = 0
        while number <= 100:
            if number % 2 != 0:
                print(number)
            number += 1
            
    # Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

    if program == 9:
        number = 0
        while number <= 100:
            if number % 5 != 0:
                print(number)
            number += 1    