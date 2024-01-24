while True:
    number_first = float(input('Enter number 1: '))
    number_second = float(input('Enter number 2: '))
    operation_type = input('What action to take? (+, -, /, *) ')

    result = 0

    if operation_type == '+':
        result = number_first + number_second
    elif operation_type == '-':
        result = number_first - number_second
    elif operation_type == '*':
        result = number_first * number_second
    elif operation_type == '/':
        if number_second != 0:
            result = number_first / number_second
        else:
            print('It is forbidden to divide by zero')
            result = print('!!!')

    print('Result:', result)

    continue_calculations = input('Do you want to continue? ')

    if continue_calculations.lower() == 'yes' or continue_calculations.lower() == 'y':
        print('Lets go')
    else:
        break
