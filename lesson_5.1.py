import string
import keyword

name = input("Enter variable name: ")

starts_with_digit = name[0].isdigit()
only_digits = name.isdigit()
invalid_values = any(value.isupper() or value in string.punctuation.replace("_", " ") for value in name)
registered_words = name in keyword.kwlist

print(not starts_with_digit and not only_digits and not invalid_values and not registered_words)

# _ => True
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
