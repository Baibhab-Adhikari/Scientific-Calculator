import calc_class as calci
# global bool flag
calculation = True


def main():
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
                print(f"Calculator mode changed to {calculator.mode}")

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
            # # ask user for continuation
            # calci.continue_calculator()

        # logarithm operations
        elif choice == 3:
            # instantiate the logarithm class and print menu
            log_calci = calci.Logarithm()
            print("Default base for logarithm is e...")
            # input x and base from user
            x, base = calci.log_input()
            calculator.current_val = log_calci.log(x, base)
            print(f"log of {x} to base {base} = {calculator.current_val}")
            # # ask user for continuation
            # calci.continue_calculator()

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
                b, p = calci.input_two_operands()
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
            # # ask user for continuation
            # calci.continue_calculator()

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
                    for r, phi in calculator.current_val:
                        print(f"r = {r}")
                        print(f"phi = {phi}")
                elif operation == 'B':
                    r, phi = calci.complex_input()
                else:
                    pass
                # # ask user for continuation
                # calci.continue_calculator()

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


if __name__ == "__main__":
    main()
