number_first = float(input('Enter number 1: '))
number_second = float(input('Enter number 2: '))

operation_type = (input('What action to take? (+, -, /, *) '))

if operation_type == '+':
    print(number_first + number_second)
elif operation_type == '-':
    print(number_first - number_second)
elif operation_type == '*':
    print(number_first * number_second)
elif operation_type == '/':
    if number_second != 0:
        print(number_first / number_second)
    else:
        print('It is forbidden to divide by zero')
