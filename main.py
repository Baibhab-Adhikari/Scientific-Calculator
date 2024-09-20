"""
Main Script for Scientific Calculator

This script serves as the entry point for the scientific calculator application.
It provides a user interface for performing various calculations, including arithmetic,
trigonometric, logarithmic, and power operations. The script also allows users to change
the calculator mode between degrees and radians.

Author: Baibhab Adhikari
Github: https://github.com/Baibhab-Adhikari
Date: July,2024

Functions:
    - main(): The main function that runs the calculator application.

Usage:
    Run this script to start the scientific calculator application. Follow the on-screen
    prompts to perform different calculations.

"""

import calc_class as calci
# global bool flag
calculation = True


def main():
    """
    

    This function initializes the calculator, displays the main menu, and handles user input
    to perform various calculations. It supports changing the calculator mode, performing
    arithmetic operations, and more.

    The function runs in a loop until the user chooses to exit the application.
    """
    global calculation
    calculator = calci.Calculator()
    while (calculation):
        # instantiate new calculator and print the user menu and reset current value
        print(f"Calculator Mode: {calculator.mode}")
        calci.print_menu()
        calci.reset_current_val(calculator)
        choice: int = -1
        while choice not in range(1, 8):
            try:
                choice = int(input("Please choose from 1 to 7: "))
            except ValueError:
                print("Invalid input. Please enter a number from 1 to 7.")

        # conditionals based on the choice of the user

        # change calculator mode
        if choice == 6:
            mode = 'X'
            while mode not in ['D', 'R']:
                mode = input("Enter D or R to change mode: ").upper()
                calculator.change_mode(mode)

        # arithmetic operations
        elif choice == 1:
            # instantiate the arithmetic class
            arithmetic_calci = calci.Arithmetic()
            # print user menu for arithmetic
            calci.print_arithmetic_menu()
            operation = 'wrong'
            while operation not in ['A', 'B', 'C', 'D']:
                operation = input(
                    "Choose any of the above, (enter a,b,c, or d): ").upper()
            # addition
            if operation == 'A':
                a, b = calci.input_two_operands()
                calculator.current_val = arithmetic_calci.addition(a, b)
                print(f"Sum of {a} and {b} is {calculator.current_val}")
            # subtraction
            elif operation == 'B':
                a, b = calci.input_two_operands()
                calculator.current_val = arithmetic_calci.subtraction(a, b)
                print(f"Difference between {a} and {
                      b} is {calculator.current_val}")
            # multiplication
            elif operation == 'C':
                a, b = calci.input_two_operands()
                calculator.current_val = arithmetic_calci.multiplication(a, b)
                print(f"Product of {a} and {b} is {calculator.current_val}")
            # division
            elif operation == 'D':
                a, b = calci.input_two_operands()
                calculator.current_val = arithmetic_calci.division(a, b)
                print(f"{a} divided by {b} is {calculator.current_val}")
            else:
                pass
            # ask user for continuation
            # calculation = calci.continue_calculator()

        # trigonometry operations
        elif choice == 2:
            trig_calci = calci.Trigonometry()
            calci.print_trigonometry_menu()
            operation = 'wrong'
            while operation not in ['A', 'B', 'C', 'D', 'E', 'F']:
                operation = input(
                    "Choose any of the above, (enter a,b,c,d,e, or f): ").upper()
            if operation == 'A':
                a = float(input("Enter the angle: "))
                result = trig_calci.sine(a, calculator.mode)
                print(f"Sine of {a} is {result}")
            elif operation == 'B':
                a = float(input("Enter the angle: "))
                result = trig_calci.cosine(a, calculator.mode)
                print(f"Cosine of {a} is {result}")
            elif operation == 'C':
                a = float(input("Enter the angle: "))
                result = trig_calci.tangent(a, calculator.mode)
                print(f"Tangent of {a} is {result}")
            elif operation == 'D':
                a = float(input("Enter the value: "))
                print(f"Current mode: {calculator.mode}")
                result = trig_calci.arcsine(a, calculator.mode)
                print(f"Arcsine of {a} is {result}")
            elif operation == 'E':
                a = float(input("Enter the value: "))
                result = trig_calci.arccosine(a, calculator.mode)
                print(f"Arccosine of {a} is {result}")
            elif operation == 'F':
                a = float(input("Enter the value: "))
                result = trig_calci.arctangent(a, calculator.mode)
                print(f"Arctangent of {a} is {result}")
            else:
                pass

        # logarithm operations
        elif choice == 3:
            # instantiate the logarithm class and print menu
            log_calci = calci.Logarithm()
            print("Default base for logarithm is e...")
            # input x and base from user
            x = calci.log_input()
            base = input("Enter base of log (leave blank for e): ")
            if base == "":
                calculator.current_val = log_calci.log(x, calci.E)
                print(f"log of {x} to base 'e' = {calculator.current_val}")
            else:
                base = float(base)
                calculator.current_val = log_calci.log(x, base)
                print(f"log of {x} to base {base} = {calculator.current_val}")

        # power/exponent operations
        elif choice == 4:
            # instantiate the power class
            power_calci = calci.Power()
            # print power class menu
            calci.print_power_menu()
            operation = 'wrong'
            while operation not in ['A', 'B', 'C']:
                operation = input(
                    "Choose any of the above, (enter a,b, or c): ").upper()
            if operation == 'A':
                b, p = calci.power_input()
                calculator.current_val = power_calci.exponent(b, p)
                print(f"{b} raised to {p} = {calculator.current_val}")
            elif operation == 'B':
                x = float(input("Enter number: "))
                calculator.current_val = power_calci.root(x)
                print(f"Square root of {x} = {calculator.current_val}")
            elif operation == 'C':
                x = float(input("Enter number: "))
                calculator.current_val = power_calci.cube_root(x)
                print(f"Cube root of {x} = {calculator.current_val}")
            else:
                pass

        # complex operations
        elif choice == 5:
            # instantiate complex class
            complex_calci = calci.Complex()
            # print complex class menu
            calci.print_complex_menu()
            operation = 'wrong'
            while operation not in ['A', 'B']:
                operation = input(
                    "Choose any of the above, (enter a or b): ").upper()

                if operation == 'A':
                    z: complex = complex(
                        input("Enter complex number in rectangular form: "))
                    calculator.current_val = complex_calci.to_polar(z)
                    print(f"Polar form of {z} = {calculator.current_val}")

                elif operation == 'B':
                    r, phi = calci.complex_input()
                    calculator.current_val = complex_calci.to_rect(r, phi)
                    print(f"Rectangular form of {r},{
                          phi} = {calculator.current_val}")
                else:
                    pass

        # exiting the calculator app
        elif choice == 7:
            calculation = False
            print("Thanks for using the Scientific Calculator!")
            print("Exiting program.....")

        # ask user for continuation
        if choice in range(1, 6):
            calculation = calci.continue_calculator()
            if not calculation:
                print("Thanks for using the Scientific Calculator!")
                print("Exiting the program.....")


if __name__ == "__main__":
    main()
