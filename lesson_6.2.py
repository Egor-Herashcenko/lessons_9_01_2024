my_dict_1 = {'key_1': 1,
             'key_2': 2,
             'key_3': 3,
}

my_dict_2 = {'key_2': 4,
             'key_3': 5,
             'key_4': 6,
}

common_keys = list(set(my_dict_1.keys()) & set(my_dict_2.keys()))
print("1):", common_keys)

keys_only_in_first = [key for key in my_dict_1.keys() if key not in my_dict_2]
print("2):", keys_only_in_first)

new_dict = {key: my_dict_1[key] for key in keys_only_in_first}
print("3):", new_dict)

merged_dict = {}

for key in keys_only_in_first:
    merged_dict[key] = my_dict_1[key]

for key in my_dict_2.keys():
    if key not in my_dict_1:
        merged_dict[key] = my_dict_2[key]

for key in common_keys:
    merged_dict[key] = [my_dict_1[key], my_dict_2[key]]

print("4):", merged_dict)
