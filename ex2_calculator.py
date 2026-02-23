# -------------------------------------------------------
# Question No: 2
# File Name : ex2_calculator.py
# Program   : Simple Calculator
# Description:
# This program takes two numbers as input and performs
# basic arithmetic operations like addition, subtraction,
# multiplication, division, modulus, and exponentiation.
# -------------------------------------------------------
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number:"))
print("Results:")
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
if num2 != 0:
    print(num1 / num2)
else: 
    print("can't divide by zero")
print(num1 % num2)

print(num1 ** num2)
