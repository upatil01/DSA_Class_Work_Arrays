def reverse_array_in_place(arr):
    length = len(arr)

    start = 0
    end = length - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]

        start += 1
        end -= 1

my_array = [1, 2, 3, 4, 5]

reverse_array_in_place(my_array)

print("Reversed array:", my_array)