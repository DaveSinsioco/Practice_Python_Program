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