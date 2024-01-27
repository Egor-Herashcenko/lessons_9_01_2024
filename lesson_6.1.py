people_list = [{"name": "John", "age": 15},
               {"name": "Denis", "age": 19},
               {"name": "Carl", "age": 15},
               {"name": "Jack", "age": 45},
               {"name": "Susan", "age": 27},
]

youngest_age = min(person["age"] for person in people_list)
youngest_names = [person["name"] for person in people_list if person["age"] == youngest_age]

longest_length = max(len(person["name"]) for person in people_list)
longest_names = [person["name"] for person in people_list if len(person["name"]) == longest_length]

average_age = sum(person["age"] for person in people_list) / len(people_list)

print("1):", youngest_names)
print("2):", longest_names)
print("3):", average_age)
