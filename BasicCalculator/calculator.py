num1 = float(input("Enter your first real number: "))
op = input("Enter your operator: ")
num2 = float(input("Enter your second real number: "))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 + num2)
elif op == '*':
    print(num1 * num2)
elif op == '/' and num2 != 0:
    print(num1 / num2)
else:
    print("Invalid input!")

# thanksgiving to python
