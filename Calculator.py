symbol = (input("What symbol would you like to use (+ | * | - | /): "))
num1 = float(input("Enter number 1 please: "))
num2 = float(input("Enter number 2 please: "))

if symbol == '+':
    sum = num1 + num2
    print(sum)
elif symbol == '*':
    sum = num1 * num2
    print(sum)
elif symbol == '-':
    sum = num1 - num2
    print(sum)
elif symbol == '/':
    sum = num1 / num2
    print(sum)
