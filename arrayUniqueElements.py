my_array = [1, 2, 2, 3, 4, 4, 5, 6, 6]

unique_array = []

for element in my_array:
    if element not in unique_array:
        unique_array.append(element)

print("Modified array with duplicates removed:", unique_array)