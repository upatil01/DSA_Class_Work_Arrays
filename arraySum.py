def calculate_array_sum(arr):
    total_sum = 0
    
    for num in arr:
        total_sum += num
    
    return total_sum

my_array = [1, 2, 3, 4, 5]

result = calculate_array_sum(my_array)

print("Sum of elements in the array:", result)