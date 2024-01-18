value_list = [1, 4, 5, 6]
if value_list:
    value_list.insert(0, value_list.pop(-1))
print(value_list)
