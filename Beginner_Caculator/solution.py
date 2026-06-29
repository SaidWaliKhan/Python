# ==========================================
# Project 01 - Python Fundamentals Playground
# Personal Information Card + Calculator
# ==========================================

print("=" * 45)
print("   Welcome to Python Fundamentals Playground")
print("=" * 45)

# ----------------------------
# Personal Information
# ----------------------------

print("\n--- Personal Information ---")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
country = input("Enter your country: ")
language = input("Enter your favorite programming language: ")

print("\n" + "=" * 35)
print("        PERSONAL CARD")
print("=" * 35)

print(f"Name     : {name}")
print(f"Age      : {age}")
print(f"Country  : {country}")
print(f"Language : {language}")

print("\nKeep learning and have fun coding!")
print("=" * 35)

# ----------------------------
# Calculator
# ----------------------------

print("\n--- Basic Calculator ---")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n===== RESULTS =====")

print(f"Addition        : {num1 + num2}")
print(f"Subtraction     : {num1 - num2}")
print(f"Multiplication  : {num1 * num2}")

if num2 != 0:
    print(f"Division        : {num1 / num2}")
    print(f"Floor Division  : {num1 // num2}")
    print(f"Modulus         : {num1 % num2}")
else:
    print("Division        : Cannot divide by zero")
    print("Floor Division  : Cannot divide by zero")
    print("Modulus         : Cannot divide by zero")

print(f"Power           : {num1 ** num2}")

print("\nThank you for using the program!")