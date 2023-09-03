def search_in_array(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1  # Return -1 if the target is not found in the array


my_array = [31,5,7,34,98,56,6,43,55]


target = 56


result = search_in_array(my_array, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found in the array")