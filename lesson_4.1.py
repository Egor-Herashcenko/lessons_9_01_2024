# value_list = [0, 4, 5, 0, 6, 0, 7]
# value_list.sort(key=lambda x: x == 0)
# print(value_list)


value_list = [1, 0, 3, 0, 0, 0, 5, 6, 0, 8, 0, 3]
for zero in range(len(value_list) - 1, -1, -1):
    if value_list[zero] == 0:
        value_list.append(value_list.pop(zero))

print(value_list)
