def find_sum_of_smallest_and_largest(arr):
    if not arr:
        return "Array is empty"

    smallest = float('inf')
    largest = float('-inf')

    for num in arr:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    result_sum = smallest + largest

    return result_sum
input_str = input("Enter integers separated by spaces: ")
integer_array = list(map(int, input_str.split()))
result = find_sum_of_smallest_and_largest(integer_array)
print("Sum of smallest and largest elements:", result)
