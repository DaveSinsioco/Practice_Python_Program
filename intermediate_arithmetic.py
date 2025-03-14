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