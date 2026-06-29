import sys

if len(sys.argv) != 3:
    print("Usage: python3 calcy.py <num1> <num2>")
    sys.exit(1)

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

print("First Number :", num1)
print("Second Number:", num2)
print("Addition      :", num1 + num2)
print("Subtraction   :", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division      :", num1 / num2)
else:
    print("Division      : Cannot divide by zero")
