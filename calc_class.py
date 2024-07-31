import math
import cmath

# global variables
E: float = math.e

# abstract Calculator class


class Calculator:

    def __init__(self) -> None:
        self.current_val = 0  # default value is 0
        self.mode = 'D'  # default mode is Degree

    def __str__(self) -> str:
        return f"The mode of calculator is {self.mode}"

    def change_mode(self, mode: str) -> None:
        if mode in ['D', 'R']:
            self.mode = mode
            print(f"Mode changed to: {self.mode}")
        else:
            print("Invalid mode. Mode not changed.")
# child arithmetic class


class Arithmetic(Calculator):

    def addition(self, a: float, b: float):
        self.current_val = a + b
        return self.current_val

    def subtraction(self, a: float, b: float):
        self.current_val = a - b
        return self.current_val

    def multiplication(self, a: float, b: float):
        self.current_val = a * b
        return self.current_val

    def division(self, a: float, b: float):
        try:
            self.current_val = float(a / b)
        except ZeroDivisionError:
            print("Cannot divide by zero!")
            self.current_val = 0
        return self.current_val
# child trigonometric class (returns angle in radians by default -> convert to degrees because calc mode is D by default)


class Trigonometry(Calculator):

    def _convert_to_radians(self, a: float) -> float:
        return math.radians(a) if self.mode == 'D' else a

    def _convert_to_degrees(self, a: float) -> float:
        return math.degrees(a) if self.mode == 'R' else a

    def sine(self, a):
        print(f"Mode: {self.mode}, Angle before conversion: {a}")
        a_rad = self._convert_to_radians(a)
        print(f"Angle in radians: {a_rad}")
        self.current_val = math.sin(a_rad)
        return self.current_val

    def cosine(self, a):
        a_rad = self._convert_to_radians(a)
        self.current_val = math.cos(a_rad)
        return self.current_val

    def tangent(self, a):
        a_rad = self._convert_to_radians(a)
        self.current_val = math.tan(a_rad)
        return self.current_val

    def arcsine(self, a):
        if not -1 <= a <= 1:
            raise ValueError("Input should be within the range [-1, 1]")
        self.current_val = math.asin(a)
        return self._convert_to_degrees(self.current_val)

    def arccosine(self, a):
        if not -1 <= a <= 1:
            raise ValueError("Input should be within the range [-1, 1]")
        self.current_val = math.acos(a)
        return self._convert_to_degrees(self.current_val)

    def arctangent(self, a):
        self.current_val = math.atan(a)
        return self._convert_to_degrees(self.current_val)


# child logarithm class


class Logarithm(Calculator):

    def log(self, a: float, base: float = math.e) -> float:
        if a <= 0:
            raise ValueError("Input 'a' must be positive.")
        if base <= 0 or base == 1:
            raise ValueError("Base must be positive and not equal to 1.")

        if base == 2:
            self.current_val = math.log2(a)
        elif base == 10:
            self.current_val = math.log10(a)
        else:
            self.current_val = math.log(a, base)

        return self.current_val

# child class for exponent operations


class Power(Calculator):

    def exponent(self, base, power):
        self.current_val = math.pow(base, power)
        return self.current_val

    def root(self, a):
        if a < 0:
            raise ValueError("Input 'a' must be non-negative for square root.")
        self.current_val = math.sqrt(a)
        return self.current_val

    def cube_root(self, a):
        self.current_val = math.cbrt(a)
        return self.current_val
# child class for complex number mathematics


class Complex(Calculator):

    def to_polar(self, z: complex) -> tuple:
        self.current_val = cmath.polar(z)
        return self.current_val

    def to_rect(self, r: float, phi: float) -> complex:
        self.current_val = cmath.rect(r, phi)
        return self.current_val


# functions for extra functionality

def reset_current_val(instance):
    instance.current_val = 0


# def change_mode(instance, mode: str):
#     instance.mode = mode
#     print(f"Calculator mode changed to {mode}")


def print_menu() -> None:
    print("Welcome to Scientific Calculator!")
    print("Choose any one of the following operations to get started!: ")
    print("1.Arithmetic")
    print("2.Trigonometry")
    print("3.Logarithm")
    print("4.Power")
    print("5.Complex")
    print(
        "6.Change Calculator Mode (Degrees(D)/ Radians(R). Degree is the default mode")
    print("7.Exit")


def print_arithmetic_menu() -> None:
    print("A.Addition")
    print("B.Subtraction")
    print("C.Multiplication")
    print("D.Division")


def print_trigonometry_menu() -> None:
    print("A.Sine")
    print("B.Cosine")
    print("C.Tangent")
    print("D.Arcsine")
    print("E.Arccos")
    print("F.Arctan")
    print("Choose from the above options (enter from a to f): ")


def print_power_menu() -> None:
    print("A.Exponent")
    print("B.Square Root")
    print("C.Cube Root")


def print_complex_menu() -> None:
    print("A.Convert Rectangular form to Polar form")
    print("B.Convert Polar form to Rectangular form")


def log_input() -> tuple:
    while True:
        try:
            x = float(input("Enter x: "))
            base = float(input("Enter base: "))
            return x, base
        except ValueError:
            print("Please enter the correct value!")


def complex_input() -> tuple:
    while True:
        try:
            a = float(input("Enter r: "))
            b = float(input("Enter phi: "))
            return a, b
        except ValueError:
            print("Please enter the correct value!")


def input_two_operands() -> tuple:
    while True:
        try:
            a = float(input("Enter first operand: "))
            b = float(input("Enter second operand: "))
            return a, b
        except ValueError:
            print("Please enter the correct value!")


def input_angle() -> float:
    while True:
        try:
            angle = float(input("Enter angle: "))
            return angle
        except ValueError:
            print("Please enter valid angle..")


def continue_calculator() -> bool:
    choice = 'wrong'
    while choice not in ['y', 'n']:
        choice = input("Do you wish to continue calculations? (y/n): ").lower()
    if choice == 'y':
        return True
    return False
