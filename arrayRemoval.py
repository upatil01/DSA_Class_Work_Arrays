my_array = [1, 2, 3, 4, 2, 5, 6, 2, 7]

value_to_remove = 2

filtered_array = [x for x in my_array if x != value_to_remove]

print("Modified array after removing", value_to_remove, ":", filtered_array)