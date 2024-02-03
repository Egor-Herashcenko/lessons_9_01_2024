def add_one(some_list):

    result = [int(digit) for digit in str(int(''.join(map(str, some_list))) + 1)]
    return result

    # num = int(''.join(map(str, some_list)))
    # num += 1
    # result_list = [int(digit) for digit in str(num)]
    #
    # return result_list

# Можно написать то же самое вот так, как по мне читабельнее, но первый вариант солиднее выглядит)))


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
