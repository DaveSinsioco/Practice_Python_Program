# Creating a loop

start = "y"
while start == "y":
    
# asking which program
    program = int(input("Program(1-10)? "))

    # Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

    if program == 1:
        num1 = int(input("1st number? "))
        num2 = int(input("2nd number? "))
        if num1 > num2:
            print(num1)
        if num1 < num2:
            print(num2)

    # Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

    if program == 2:
        num1 = int(input("1st number? "))
        num2 = int(input("2nd number? "))
        if num1 == num2:
            print("Equal")        

    # Prog03: Create a program that ask user to input 2 numbers. Print the sum of the two numbers.

    if program == 3:
        num1 = int(input("1st number? "))
        num2 = int(input("2nd number? "))
        print(f"{num1 + num2}")

    # Prog04: Create a program that ask user to input 2 numbers. Print the product of the two numbers.

    if program == 4:
        num1 = int(input("1st number? "))
        num2 = int(input("2nd number? "))
        print(f"{num1 * num2}")

    # Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point

    if program == 5:
        num1 = int(input("1st number? "))
        num2 = int(input("2nd number? "))
        print(f"{float(num1 / num2)}")
        
    # Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.

    if program == 6:
        num1 = int(input("1st number? "))
        num2 = int(input("2nd number? "))
        print(f"{num1 ** num2}")        