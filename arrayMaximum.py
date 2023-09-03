my_array = [10, 5, 8, 12, 7, 3, 15, 9]


max_value = my_array[0] 
max_index = 0


for i in range(1, len(my_array)):
    if my_array[i] > max_value:
        max_value = my_array[i]
        max_index = i

print("Maximum value:", max_value)
print("Index of maximum value:", max_index)