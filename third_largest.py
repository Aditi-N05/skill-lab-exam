def third_largest(arr):
    if len(arr) < 3:
        return ("Array must have at least 3 elements")

    first = second = third = float('-inf')

    for number in arr:
        if number > first:
            third = second
            second = first
            first = number
        elif number > second and number != first:
            third = second
            second = number
        elif number > third and number != second and number != first:
            third = number

    return third if third != float('-inf') else "No third distinct largest element"

# Example:
arr = [12, 45, 1, -1, 45, 54, 23, 5]
print("Third largest element is:", third_largest(arr))
