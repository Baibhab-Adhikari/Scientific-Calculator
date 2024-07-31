"""
Calculator Class Module

This module provides classes and methods for performing various scientific calculations,
including arithmetic operations, trigonometric functions, and logarithmic calculations.

Author: Baibhab Adhikari
Github: https://github.com/Baibhab-Adhikari
Date: July,2024

Classes:
    - Calculator: Base class for scientific calculator operations.
    - Arithmetic: Handles basic arithmetic operations.
    - Trigonometry: Performs trigonometric calculations with angle mode conversion.
    - Power: Handles power and root calculations.
    - Complex: Performs operations on complex numbers.
    - Log: Handles logarithmic calculations.

Global Variables:
    - E: The mathematical constant e (Euler's number).

Usage:
    This module can be imported and used to create instances of the Calculator,
    Arithmetic, and Trigonometry classes to perform various calculations.


"""
# imports
import math
import cmath

# global variables
E: float = math.e

# abstract Calculator class


class Calculator:
    """
    Base class for scientific calculator operations.

    Manages the current value and angle mode (degrees or radians).
    Provides methods for changing mode and resetting current value.
    """

    def __init__(self) -> None:
        self.current_val = 0  # default value is 0
        self.mode = 'D'  # default mode is Degree

    def __str__(self) -> str:
        return f"The mode of calculator is {self.mode}"

    def change_mode(self, mode: str) -> None:
        if mode in ['D', 'R']:
            self.mode = mode
        else:
            print("Invalid mode. Mode not changed.")
# child arithmetic class


class Arithmetic(Calculator):
    """
    Handles basic arithmetic operations.

    Supports addition, subtraction, multiplication, and division.
    Inherits mode and current value management from Calculator.
    """

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


class Trigonometry:
    """
    Performs trigonometric calculations with angle mode conversion.

    Supports sine, cosine, tangent, and their inverse functions.
    Handles conversions between degrees and radians based on the specified mode.
    """

    def _convert_to_radians(self, a: float, mode: str) -> float:
        return math.radians(a) if mode == 'D' else a

    def _convert_to_degrees(self, a: float, mode: str) -> float:
        return math.degrees(a) if mode == 'D' else a

    def sine(self, a, mode):
        a_rad = self._convert_to_radians(a, mode)
        return math.sin(a_rad)

    def cosine(self, a, mode):
        a_rad = self._convert_to_radians(a, mode)
        return round(math.cos(a_rad), 10)  # Round to 10 decimal places

    def tangent(self, a, mode):
        if mode == 'D' and (a % 180 == 90):
            raise ValueError("Tangent is undefined for 90 + k*180 degrees")
        a_rad = self._convert_to_radians(a, mode)
        return math.tan(a_rad)

    def arcsine(self, a, mode):
        if not -1 <= a <= 1:
            raise ValueError("Input should be within the range [-1, 1]")
        result = math.asin(a)
        return self._convert_to_degrees(result, mode)

    def arccosine(self, a, mode):
        if not -1 <= a <= 1:
            raise ValueError("Input should be within the range [-1, 1]")
        result = math.acos(a)
        return self._convert_to_degrees(result, mode)

    def arctangent(self, a, mode):
        result = math.atan(a)
        return self._convert_to_degrees(result, mode)


# child logarithm class


class Logarithm(Calculator):
    """
    Computes logarithms with various bases.

    Supports natural log, base-2 log, base-10 log, and custom base logarithms.
    Inherits mode and current value management from Calculator.
    """

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
    """
    Handles exponentiation and root operations.

    Supports raising to a power, square root, and cube root calculations.
    Inherits mode and current value management from Calculator.
    """

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
    """
    Manages complex number operations and conversions.

    Supports conversion between rectangular and polar forms of complex numbers.
    Inherits mode and current value management from Calculator.
    """

    def to_polar(self, z: complex) -> tuple:
        self.current_val = cmath.polar(z)
        return self.current_val

    def to_rect(self, r: float, phi: float) -> complex:
        self.current_val = cmath.rect(r, phi)
        return self.current_val


# functions for extra functionality

def reset_current_val(instance):
    """
    Resets the current value of the calculator instance to zero.

    Args:
        instance: The calculator instance whose current value is to be reset.
    """
    instance.current_val = 0


def print_menu() -> None:
    """
    Displays the main menu of the scientific calculator.

    Presents options for different types of calculations and mode changes.
    """
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
    """
    Displays the arithmetic operations menu.

    Lists the available arithmetic operations: Addition, Subtraction, Multiplication, and Division.
    """
    print("A.Addition")
    print("B.Subtraction")
    print("C.Multiplication")
    print("D.Division")


def print_trigonometry_menu() -> None:
    """
    Displays the trigonometry operations menu.

    Lists the available trigonometric operations: Sine, Cosine, Tangent, Arcsine, Arccos, and Arctan.
    """
    print("A.Sine")
    print("B.Cosine")
    print("C.Tangent")
    print("D.Arcsine")
    print("E.Arccos")
    print("F.Arctan")
    print("Choose from the above options (enter from a to f): ")


def print_power_menu() -> None:
    """
    Displays the power operations menu.

    Lists the available power operations: Exponent, Square Root, and Cube Root.
    """
    print("A.Exponent")
    print("B.Square Root")
    print("C.Cube Root")


def print_complex_menu() -> None:
    """
    Displays the complex number operations menu.

    Lists the available complex number operations: Convert Rectangular form to Polar form, and Convert Polar form to Rectangular form.
    """
    print("A.Convert Rectangular form to Polar form")
    print("B.Convert Polar form to Rectangular form")


def log_input() -> tuple:
    """
    Prompts the user to enter a value for logarithmic calculations.

    Repeatedly prompts the user until a valid float is entered.

    Returns:
        float: The value entered by the user.
    """
    while True:
        try:
            x = float(input("Enter x: "))
            return x
        except ValueError:
            print("Please enter the correct value!")


def complex_input() -> tuple:
    """
    Prompts for and returns two float operands for binary operations.

    Returns:
        tuple: A pair of float values representing the two operands.

    Raises:
        ValueError: If the input cannot be converted to float.
    """
    while True:
        try:
            a = float(input("Enter r: "))
            b = float(input("Enter phi: "))
            return a, b
        except ValueError:
            print("Please enter the correct value!")


def power_input() -> tuple:
    """
    Prompts for and returns two float operands for binary operations.

    Returns:
        tuple: A pair of float values representing the two operands.

    Raises:
        ValueError: If the input cannot be converted to float.
    """
    while True:
        try:
            a = float(input("Enter base: "))
            b = float(input("Enter power: "))
            return a, b
        except ValueError:
            print("Please enter the correct value!")


def input_two_operands() -> tuple:
    """
    Prompts for and returns two float operands for binary operations.

    Returns:
        tuple: A pair of float values representing the two operands.

    Raises:
        ValueError: If the input cannot be converted to float.
    """
    while True:
        try:
            a = float(input("Enter first operand: "))
            b = float(input("Enter second operand: "))
            return a, b
        except ValueError:
            print("Please enter the correct value!")


def input_angle() -> float:
    """
    Prompt the user to enter an angle and return it as a float.

    This function repeatedly prompts the user to enter a valid angle until a valid float is provided.
    If the user enters an invalid value, an error message is displayed and the user is prompted again.

    Returns:
        float: The angle entered by the user.
    """
    while True:
        try:
            angle = float(input("Enter angle: "))
            return angle
        except ValueError:
            print("Please enter valid angle..")


def continue_calculator() -> bool:
    """
    Asks if the user wants to continue using the calculator.

    Returns:
        bool: True if the user wants to continue, False otherwise.
    """
    choice = 'wrong'
    while choice not in ['y', 'n']:
        choice = input("Do you wish to continue calculations? (y/n): ").lower()
    if choice == 'y':
        return True
    return False
